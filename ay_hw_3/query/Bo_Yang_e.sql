SELECT
	a.grade,
	avg(a.score)
FROM
	inspections a
GROUP BY
	a.grade
HAVING
	a.grade IN ('A', 'B', 'C')