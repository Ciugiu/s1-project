SELECT 
    CONTACT_EMAIL,  
    CONTACT_FIRST_NAME, 
    CONTACT_LAST_NAME, 
    COURSE_NAME, 
    sum_in/cnt AS sum_out
FROM (
    SELECT 
        GRADE_STUDENT_EPITA_EMAIL_REF, 
        GRADE_COURSE_CODE_REF,
        cn.COURSE_NAME, 
        SUM(GRADE_SCORE) AS sum_in, 
        COUNT(GRADE_SCORE) AS cnt
    FROM 
        GRADES
    JOIN (
        SELECT 
            COURSE_CODE, 
            COURSE_NAME  
        FROM 
            COURSES
    ) AS cn ON cn.COURSE_CODE  = GRADE_COURSE_CODE_REF
    GROUP BY 
        GRADE_COURSE_CODE_REF, 
        GRADE_STUDENT_EPITA_EMAIL_REF,
        cn.COURSE_NAME
) g
JOIN 
    STUDENTS s ON g.GRADE_STUDENT_EPITA_EMAIL_REF = s.STUDENT_EPITA_EMAIL
JOIN 
    CONTACTS c ON s.STUDENT_CONTACT_REF = c.CONTACT_EMAIL
WHERE 
    s.STUDENT_POPULATION_PERIOD_REF = %s
    AND s.STUDENT_POPULATION_YEAR_REF = %s
    AND s.STUDENT_POPULATION_CODE_REF = %s
ORDER BY 
    g.GRADE_STUDENT_EPITA_EMAIL_REF