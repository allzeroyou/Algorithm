-- 코드를 작성해주세요
select f.ITEM_ID, f.ITEM_NAME
from ITEM_INFO f
join 
(select *
from ITEM_TREE
where PARENT_ITEM_ID is null) t
ON f.ITEM_ID=t.ITEM_ID;
