SELECT DISTINCT
	(a.facility_name)
FROM
	inspections a
WHERE
	a.facility_id NOT IN (
		SELECT DISTINCT
			(b.facility_id)
		FROM
			violations b
	)
ORDER BY
	a.facility_name