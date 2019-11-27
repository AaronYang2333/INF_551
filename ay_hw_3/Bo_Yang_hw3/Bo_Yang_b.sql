SELECT
	a.facility_name
FROM
	inspections a
WHERE
	a.score >= ALL (
		SELECT
			max(score)
		FROM
			inspections
	)
GROUP BY
	a.facility_name



