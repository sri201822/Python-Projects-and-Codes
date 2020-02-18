#query
SELECT * FROM information_schema.columns WHERE table_schema = 'xyz' order by column_name;
select distinct(column_name) from information_schema.columns where table_schema='xyz';
