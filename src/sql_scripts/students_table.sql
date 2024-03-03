SELECT
    STUDENT_CONTACT_REF, 
    CONTACT_FIRST_NAME, 
    CONTACT_LAST_NAME, 
    passed
FROM (
    SELECT 
        GRADE_STUDENT_EPITA_EMAIL_REF, 
        STUDENT_CONTACT_REF, 
        STUDENT_POPULATION_PERIOD_REF, 
        STUDENT_POPULATION_YEAR_REF, 
        STUDENT_POPULATION_CODE_REF, 
        CONTACT_FIRST_NAME, 
        CONTACT_LAST_NAME, 
        COUNT(
            CASE WHEN sum_out > 10 THEN 1 END
        ) AS passed
    FROM (
        SELECT 
            *, 
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
            ) AS cn ON cn.COURSE_CODE = GRADE_COURSE_CODE_REF
            GROUP BY 
                GRADE_COURSE_CODE_REF,
                GRADE_STUDENT_EPITA_EMAIL_REF,
                cn.COURSE_NAME
            ORDER BY 
                GRADE_STUDENT_EPITA_EMAIL_REF
        ) g
        JOIN 
            STUDENTS s ON g.GRADE_STUDENT_EPITA_EMAIL_REF = s.STUDENT_EPITA_EMAIL
        JOIN 
            CONTACTS c ON s.STUDENT_CONTACT_REF = c.CONTACT_EMAIL
    ) sub
    GROUP BY 
        GRADE_STUDENT_EPITA_EMAIL_REF, 
        STUDENT_CONTACT_REF,
        STUDENT_POPULATION_PERIOD_REF, 
        STUDENT_POPULATION_YEAR_REF, 
        STUDENT_POPULATION_CODE_REF, 
        CONTACT_FIRST_NAME, 
        CONTACT_LAST_NAME
) sub2
WHERE 
    STUDENT_POPULATION_CODE_REF = %s
    AND STUDENT_POPULATION_YEAR_REF = %s
    AND STUDENT_POPULATION_PERIOD_REF = %s