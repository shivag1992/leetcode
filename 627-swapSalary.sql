# Write your MySQL query statement below
#ascii('m') ^ ascii(f) = 11
update salary set sex = char(ascii(sex) ^ 11);
