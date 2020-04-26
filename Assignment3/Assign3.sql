-- Ananya Vittal
-- 2270341

CREATE TABLE Students (
    StudentId INT PRIMARY KEY AUTO_INCREMENT,
    StudentName     VARCHAR(32),
    BirthDate       DATETIME,
    Email           VARCHAR(32),
    Phone           VARCHAR(32),
    City            VARCHAR(32),
    State           VARCHAR(32),
    ZipCode         CHAR(5),
    Country         VARCHAR(100)
);

CREATE TABLE Classes (
    ClassId INT AUTO_INCREMENT,
    ClassName   VARCHAR(10),
    PRIMARY KEY (ClassId, ClassName)
);

CREATE TABLE ClassRegistration(
    StudentId   INT,
    ClassId     INT,
    FOREIGN KEY (StudentId) REFERENCES Students (StudentId),
    FOREIGN KEY (ClassId) REFERENCES Classes (ClassId)
);

CREATE TABLE Professors(
    ProfessorId INT PRIMARY KEY AUTO_INCREMENT,
    ProfessorName   VARCHAR(32)
);

CREATE TABLE Departments(
    DepartmentId INT PRIMARY KEY AUTO_INCREMENT,
    ProfessorId   INT,
    DepartmentName  VARCHAR(32),
    FOREIGN KEY (ProfessorId) REFERENCES Professors (ProfessorId)
);

