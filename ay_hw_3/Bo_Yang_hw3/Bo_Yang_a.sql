SELECT
	a.facility_name
FROM
	violations a
WHERE
	a.facility_name LIKE '%cafe%'
AND a.violation_code = 'F030'
GROUP BY
	a.facility_name