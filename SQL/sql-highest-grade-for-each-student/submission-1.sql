-- Write your query below
with score_ranked as (
    select student_id, exam_id, score,
    row_number() over(partition by student_id order by score desc, exam_id asc) as ranked
    from exam_results
)
select student_id, exam_id, score
from score_ranked
where ranked = 1;