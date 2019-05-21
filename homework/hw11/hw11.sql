CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name as dog_name, b.size as dog_size FROM dogs as a, sizes as b where a.height <= b.max and a.height > b.min;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child FROM parents AS a, dogs AS b where a.parent = b.name ORDER by b.height DESC ;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS child1,b.child AS child2 FROM parents as a, parents as b WHERE a.parent = b.parent
  AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.child1 || ' and ' || a.child2 || ' are ' || b.dog_size || ' siblings' FROM siblings as a, size_of_dogs as b,size_of_dogs as c
  WHERE a.child1 = b.dog_name
  AND a.child2 = c.dog_name AND c.dog_size = b.dog_size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
-- i don't know how this helper works
-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT a.name,b.name,c.name,d.name,a.height+b.height+c.height+d.height
  FROM dogs as a,dogs as b,dogs as c,dogs as d
  WHERE a.height < b.height AND b.height < c.height AND c.height< d.height AND a.height+b.height+c.height+d.height> 170
  ORDER by a.height+b.height+c.height+d.height;
