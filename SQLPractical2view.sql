select * from [dbo].[SQLPractical]
select* from [dbo].[SQLPractical] where embarked ='Southampton'
select Gender, Age from [dbo].[SQLPractical] where embarked ='Cherbourg'and Age = 22

select * from [dbo].[SQLPractical] order by Age asc


SELECT *
FROM  SQLPractical INNER JOIN
         Table_2 ON SQLPractical.TitanicID = Table_2.Titanicid