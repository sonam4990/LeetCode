-- select name from coustomer where referee_id<>2 or referee_id is null;
SELECT name
FROM Customer
WHERE referee_id <> 2
   OR referee_id IS NULL;