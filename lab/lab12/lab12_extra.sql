.read lab12.sql

-- Q5
CREATE TABLE fa18favpets AS
  SELECT pet , COUNT(*) FROM students GROUP BY pet ORDER BY count(*) DESC LIMIT 10;


CREATE TABLE fa18dog AS
  SELECT pet FROM students GROUP by pet HAVING pet = "dog";  -- used for test group by statement
  -- equals to SELECT pet,count(*) FROM students WHERE pet = "dog";


CREATE TABLE fa18alldogs AS
  SELECT pet,count(*) FROM students WHERE pet Like '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero,count(*) FROM students WHERE seven = '7' GROUP by denero;   -- 先把=7 的找出来 再group一下

-- Q6
CREATE TABLE smallest_int_count AS
  SELECT smallest ,count(*) FROM students GROUP by smallest ORDER by smallest;
