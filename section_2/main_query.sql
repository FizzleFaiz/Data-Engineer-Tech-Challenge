-- list of our customers and their spending
select cust_name, sum(car_price) as total_spending
from my_database.sales_trans
group by cust_name

/* 
find out the top 3 
car manufacturers that customers bought 
by sales (quantity) 
and the sales number for it in the current month
*/
select car_manu, sum(car_price) as total_sales
from my_database.sales_trans
where car_manu IN (
select top 3 car_manu, count(sales_id)
from my_database.sales_trans
where TO_CHAR(sales_ts,'MM')= MONTH(getdate())
group by car_manu)
group by car_manu