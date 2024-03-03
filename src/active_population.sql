SELECT 
    student_population_code_ref, 
    student_population_period_ref, 
    student_population_year_ref, 
    COUNT(*) as cnt
FROM 
    students
GROUP BY 
    student_population_code_ref, 
    student_population_year_ref, 
    student_population_period_ref
ORDER BY 
    cnt DESC
