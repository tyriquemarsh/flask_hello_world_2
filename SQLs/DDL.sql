Create Table Technical_Skills(
    ID integer primary key,
    Skill_Name text,
    Proficiency_Level text
);

Create Table Soft_Skills(
    ID integer primary key,
    Skill_Name text,
    Proficiency_Level text
);

Create Table Education(
    ID integer primary key,
    Qualification text,
    Institution text,
    Start_Year integer,
    End_Year integer,
    Description text
);

Create Table Work(
    ID integer primary key,
    Company_Name text,
    Job_Title text,
    Start_Date date,
    End_Date date,
    Responsibilities text
);

Create Table Contact_Messages(
    ID integer primary key,
    Name text,
    Email text unique,
    Message text
);