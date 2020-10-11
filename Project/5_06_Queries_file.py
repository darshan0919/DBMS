def give_answer(i):
    if i==1:
        return "SELECT forest_location.fname FROM forest_location GROUP BY forest_location.fname HAVING COUNT(forest_location.province)>1 EXCEPT SELECT t1.fname FROM (SELECT DISTINCT fname,country FROM forest_location) AS t1 GROUP BY t1.fname HAVING count(t1.country)>1;"

    elif i==2:
        return "SELECT e.fname,officials.name,officials.post,officials.email,officials.contact FROM officials INNER JOIN forest_location e ON officials.forest_id=e.id INNER JOIN lives_in ON e.fname=lives_in.forest_name WHERE lives_in.animal_name='Spotted Deer';"

    elif i==3:
        return "SELECT * FROM forest INNER JOIN (SELECT forest_name FROM national_park NATURAL JOIN lives_in WHERE animal_name='Tiger' EXCEPT SELECT forest_name FROM sanctuary WHERE animal = 'Tiger') AS r ON forest.name = r.forest_name;"

    elif i==4:
        return "SELECT avg(j.fraction_area), j.cause FROM ( SELECT (f.affected_area_km2/forest.area_km2) fraction_area,f.* FROM forest_fire f INNER JOIN forest_location l ON l.id=f.forest_id INNER JOIN forest ON forest.name=l.fname ) j GROUP BY cause;"

    elif i==5:
        state = input("Enter state : ")
        q = "SELECT DISTINCT tourist.name, tourist.country FROM (hotel JOIN ((h_address NATURAL JOIN package) AS t1 NATURAL JOIN selects) AS  t2 ON(hotel.id=t2.hotel_id)) AS t3 JOIN tourist ON(tourist.id=t3.tourist_id) WHERE t3.province = '{}';"
        q = q.format(state)
        return q

    elif i==6:
        return "SELECT e.year,e.name,e.frac_area FROM ( SELECT (ff.affected_area_km2/f.area_km2) as frac_area, f.name,ff.year FROM forest_fire ff INNER JOIN forest_location fl ON fl.id=ff.forest_id INNER JOIN forest f ON f.name=fl.fname ) e INNER JOIN ( SELECT max(e.frac_area),e.year FROM( SELECT (ff.affected_area_km2/f.area_km2) as frac_area, f.name,ff.year FROM forest_fire ff INNER JOIN forest_location fl ON fl.id=ff.forest_id INNER JOIN forest f ON f.name=fl.fname ) e GROUP BY e.year )g ON g.max=e.frac_area ORDER BY e.year;"

    elif i==7:
        return "SELECT t2.fname, officials.name, officials.contact, t2.fire_area FROM officials JOIN (forest_location JOIN (SELECT forest_fire.forest_id, SUM(forest_fire.affected_area_km2) AS fire_area FROM forest_fire GROUP BY forest_id ORDER BY fire_area DESC) AS t1 ON(forest_location.id=t1.forest_id)) AS t2 ON(officials.forest_id=t2.id) ORDER BY t2.fire_area DESC LIMIT 1;"

    elif i==8:
        return "SELECT fl.fname,e.treatment_type,e.average_vegetation_index,e.total_area_treated FROM( SELECT avg(i.vegetation) average_vegetation_index,sum(r.area) total_area_treated,r.treatment_type,r.forest_id FROM regeneration r NATURAL JOIN index i GROUP BY r.treatment_type,r.forest_id ) e INNER JOIN forest_location fl ON fl.id=e.forest_id ORDER BY fl.fname,e.treatment_type;"

    elif i==9:
        cause = ['Industry', 'Incendiary', 'Lightning', 'Other', 'Railway', 'Recreation', 'Residents', 'Unspecified']
        print(cause)
        cause = input("Enter cause : ")
        q = "SELECT fname AS forest_name,fire_year,fire_year_vegetation,last_year,last_vegetation FROM forest_location NATURAL JOIN (SELECT curr_veg.forest_id,fire_year,fire_year_vegetation,last_year,last_vegetation FROM (SELECT veg_idx.forest_id,veg_idx.year AS fire_year,vegetation AS fire_year_vegetation FROM (SELECT year,forest_id,vegetation FROM index) as veg_idx INNER join (SELECT * FROM forest_fire where cause = '{}') AS fire_year ON fire_year.year=veg_idx.year AND fire_year.forest_id = veg_idx.forest_id) AS curr_veg INNER join (SELECT veg_idx.forest_id,veg_idx.year AS last_year,vegetation AS last_vegetation FROM (SELECT year,forest_id,vegetation FROM index) AS veg_idx  INNER JOIN  (SELECT * FROM forest_fire WHERE cause = 'Residents') AS fire_year ON fire_year.year-1=veg_idx.year AND fire_year.forest_id = veg_idx.forest_id) AS last_veg ON curr_veg.forest_id = last_veg.forest_id AND curr_veg.fire_year-1 = last_veg.last_year) AS data;"
        q = q.format(cause)
        return q
        
    elif i==10:
        return "SELECT insect.common_name ,e.year ,e.prod_type ,e.total_defoliated_area ,e.total_treated_area FROM( SELECT ri.scientific_name,ri.year,pc.prod_type,sum(ri.defoliated_area) total_defoliated_area,sum(pc.area_km2) total_treated_area FROM forest_location fl INNER JOIN defoliates ri ON ri.forest_id=fl.id INNER JOIN pest_control pc ON pc.forest_id=fl.id and pc.insect_pest=ri.scientific_name GROUP BY ri.year,ri.scientific_name,pc.prod_type ORDER BY ri.scientific_name,ri.year,pc.prod_type ) e NATURAL JOIN insect;"

    elif i==11:
        return "SELECT fl.fname,tt.year,tt.total_tourist,rr.amount_rev FROM( SELECT tou.year,count(vb.tourist_id) total_tourist,vb.forest_id FROM tourist tou INNER JOIN visited_by vb ON vb.tourist_id=tou.id GROUP BY tou.year,vb.forest_id ) tt NATURAL JOIN( SELECT sum(re.amount$) amount_rev,re.year,re.forest_id FROM revenue re WHERE re.category='Rent' or re.category='Sales_and_Rentals' GROUP BY re.year,re.forest_id ) rr  INNER JOIN forest_location fl ON fl.id=rr.forest_id ORDER BY forest_id,year;"

    elif i==12:
        return "SELECT fname,year,avg_qty_m3,amount$ FROM forest_location INNER JOIN (SELECT * FROM (SELECT forest_id,year,AVG(quantity_m3) AS avg_qty_m3 FROM wood_supply GROUP BY forest_id,year)AS year_supply NATURAL JOIN (SELECT * FROM revenue WHERE category='Stumpage Charges') AS year_stump)AS data ON forest_location.id = data.forest_id;"

    elif i==13:
        return "SELECT lives_in.forest_name FROM lives_in INNER JOIN animal ON animal.name=lives_in.animal_name GROUP BY lives_in.forest_name HAVING max(cast(SUBSTRING(lifespan_years,4,LENGTH(lifespan_years)) as int))<=25;"

    elif i==14:
        return "SELECT * FROM lives_in WHERE animal_name not in ( SELECT animal_name FROM ( (SELECT animal_name , forest_name FROM (select forest_name from ( select forest_name,animal_name from animal_yearwise where constatus='Near Threatened' and year=2011) as s) as p cross join (select distinct animal_name from lives_in) as sp) EXCEPT (SELECT animal_name , forest_name FROM lives_in) ) AS r );"

    elif i==15:
        return "SELECT * FROM cnt_tourist();"

    elif i==16:
        return "SELECT * FROM find_popularity();"




def insert():
    table = input("Enter name of the table : ")
    print("Enter your data using ';'.")
    line = input().split(';')
    val = "INSERT INTO "+table+" VALUES ( "
    for data in line:
        val += "'"+str(data)+"', "
    val = val[:-2]
    val += " );"
    return val
    
    

# 5 - 'Gujarat'
# 9 - 'Residents'
