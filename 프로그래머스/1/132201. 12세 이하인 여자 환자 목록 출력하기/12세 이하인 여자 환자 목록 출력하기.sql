-- 코드를 입력하세요
# SELECT * from PATIENT; 
select 
PT_NAME,
PT_NO, 
GEND_CD, 
AGE,
IFNULL(TLNO, 'NONE') AS TLNO
from PATIENT 
where AGE <= 12 and GEND_CD = 'W' 
order by 
    age DESC,  -- 나이를 기준으로 내림차순 정렬
    PT_NAME;  -- 나이가 같다면, 환자 이름을 기준으로 오름차순 정렬