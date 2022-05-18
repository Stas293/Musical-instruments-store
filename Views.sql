#1
create view All_instruments as 
select * 
	from instrument_list;

#2
create view Instruments_cond as 
select * 
	from instrument_list
    where closed = 0;
    
#3
create view Instruments_cond_1 as
select *
	from instrument_list 
    where closed = 0
    and price < 200;
    
#4
create view View_instruments as
select title, description, status_id, price, closed, date_created, date_updated
	from instrument_list;

#5
create view View_instruments_ps as 
select title as Title, description as Description, status_id as Status, price as Price, closed as IsClosed, date_created as Created, date_updated as Updated
	from instrument_list
    where closed = 0;
    
#6
create view Title_desc_instruments as
select concat(title, ' Is a ', description) as Title_Description
	from instrument_list
	where closed = 0;

#7
create view Case_instruments as
select title as Title, description as Description, price as Price,
	case when price <= 200 then 'cheap'
		when price > 300 then 'expensive'
        else 'OK'
	end as Budget
from instrument_list;

#8
create view Limit_instruments as
select *
	from instrument_list
    limit 10;

#9
create view Random_instruments as
select *
		from instrument_list
		order by rand() limit 5;

#10
create view Null_instruments as
select *
		from instrument_list
		where date_created is null;
        
#11
create view Like_instruments as
select *
	from instrument_list
    where (title like '%i%' or description like '%er%');

#12
create view Sort_order_history as
select *
	from order_history
    order by rating desc;
    
#13
create view Sort1_order_history as
select *
	from order_history
    order by rating desc, total_sum;

#14
create view Substring_instruments as
select *
	from instrument_list
	order by substr(title,length(title)-2);

#15
create view Sort_null_instruments as
select title as Title, description as Description, date_created as Created
	from (
	select title, description, date_created,
		case when date_created is null then 0 else 1 end as is_null
		from instrument_list) x
	order by is_null, date_created desc;

#16
create view Sort_status_instruments as
select title as Title, description as Description, status_id as Status, price as Price
		from instrument_list
		order by case when status_id = 1 then price else title end;

#17
create view Status_instruments as
select title as Title_and_Status, status_id
 from instrument_list
union all
select '----------', null
union all
select name, status_id
from status;

#18
create view Join_status_instruments as	
select i.title, i.description, s.status_id, s.name
	from instrument_list i inner join status s
	on i.status_id = s.status_id;

#19
create view Join1_status_instruments as	
select i.title,i.description,i.status_id,v.name, i.price
 from instrument_list i, Join_status_instruments v
where i.title = v.title
  and i.description = v.description
  and i.status_id   = v.status_id;

#20
create view Not_status_instruments as
select status_id
	from status
	where status_id not in (select status_id from instrument_list);

#21
create view Outer_status_instruments as
select s.*
	from status s left outer join instrument_list i
		on (s.status_id = i.status_id);
        
#22
create view User_list_role as
select u.*, r.*
 from user_list u join user_role ur
   on (u.user_id=ur.user_id)
 left join role r
   on (ur.role_id=r.role_id)
order by 1;

#23
create view History_user as
select user_id,
    login,
	sum(total_sum) as Spent
from (
    select u.user_id,
    u.login,
    oh.total_sum
from user_list u, order_history oh
where u.user_id = oh.user_id
	)x
group by user_id;

#24
create view History_user_lo as
select user_id,
	login,
	sum(total_sum) as Cost
from (
    select us.user_id,
    us.login,
    ou.total_sum
	from user_list us left outer join order_history ou
		on (us.user_id = ou.user_id)
	)x
 group by user_id;

#25
create view Order_status_fo as
select o.order_id, o.date_created, o.user_id, o.title, o.status_id, s.name
	from order_list o right outer join status s
		on (o.status_id=s.status_id)
	union
select o.order_id, o.date_created, o.user_id, o.title, o.status_id, s.name
	from order_list o left outer join status s
		on (o.status_id=s.status_id)
order by order_id;

#26
create view HOrder_l as
select o.user_id, u.login, o.total_sum
	from order_history o right outer join user_list u
		on (o.user_id=u.user_id)
	union
select o.user_id, u.login, o.total_sum
	from order_history o left outer join user_list u
		on (o.user_id=u.user_id)
where coalesce(total_sum,0) < (100)
order by user_id;

#27
create view divide as
select substr(u.login, iter.pos, 1) as C
	from (select login from user_list where login = 'userS') u,
		(select pos from t10) iter
where iter.pos <= length(u.login);

#28
create view lapki as
select 'Good day', 'Hard day''s night';

#29
create view delete_s as
select user_id, login, replace(login, 'e', '') as striped1, password, replace(password, 3, '') as striped2
from user_list;

#30
create view divide_num_str as
select login, replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(login, 1, ''), 2, ''), 3, ''), 4, ''), 5, ''), 6, ''), 7, ''), 8, ''), 9, ''), 0, '')  as striped2,
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(
replace(login,'a',''),'b',''),'c',''),'d',''),'e',''), 'f', ''), 'g',''),'h',''),'i',''),'j',''),'k',''), 'l', ''), 'm',''),'n',''),'o',''),'p',''),'q',''), 'r', ''), 's',''),'t',''),'u',''),'v',''),'w',''), 'x', ''), 'y',''),'z',''), 'A',''),'B',''),'C',''),'D',''),'E',''), 'F', ''), 'G',''),'H',''),'I',''),'J',''),'K',''), 'L', ''), 'M',''),'N',''),'O',''),'P',''),'Q',''), 'R', ''), 'S',''),'T',''),'U',''),'V',''),'W',''), 'X', ''), 'Y',''),'Z','')
as striped1 from user_list;

#33
create view minmax_history as
select user_id, min(total_sum) as min_sum, max(total_sum) as max_sum
	from order_history
	group by user_id;

#34
create view count_history as
select user_id, count(*) as Number_of_purchases
	from order_history
	group by user_id;

#35
create view nnull_order as
select count(order_id) as Orders
	from order_status_fo;

#36
create view cur_sum_history as
select o.user_id, o.title, o.total_sum,
      (select sum(d.total_sum) from order_history d
        where d.history_id <= o.history_id) as running_total
	from order_history o 
order by 3;

#37
create view instrument_date_diff as
select instrument_id, title, datediff(date_created,date_updated) as Update_date
from instrument_list;

#39
create view number_of_days as
select day(	last_day(
			date_add(
			date_add(
			date_add(current_date, interval -dayofyear(current_date) day),
					interval 1 day),
					interval 1 month)));

#40
create view first_last as
select 	date_add(current_date,
				interval -day(current_date)+1 day) firstday,
		last_day(current_date) lastday;