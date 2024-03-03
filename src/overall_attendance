SELECT 
    s.student_population_code_ref, 
    s.student_population_period_ref, 
    s.student_population_year_ref, 
    SUM(att.attendance_presence)*100/COUNT(*) as percents
FROM 
    attendance as att
INNER JOIN 
    students as s ON s.student_epita_email = att.attendance_student_ref
GROUP BY 
    s.student_population_code_ref, 
    s.student_population_period_ref, 
    s.student_population_year_ref
ORDER BY 
    percents DESC
