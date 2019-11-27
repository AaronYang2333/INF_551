SELECT
	a.facility_name
FROM
	violations a
WHERE
	a.facility_id = (
		SELECT
			a.facility_id
		FROM
			violations a
		GROUP BY
			a.facility_id
		ORDER BY
			count(a.facility_id) DESC
		LIMIT 1
	)
LIMIT 1