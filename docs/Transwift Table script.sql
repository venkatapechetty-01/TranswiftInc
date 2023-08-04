USE MASTER
DROP DATABASE IF EXISTS TranswiftInc
CREATE DATABASE TranswiftInc

USE TranswiftInc

-- Role Table
CREATE TABLE dbo.[Role] (
    RoleID INT PRIMARY KEY,
    RoleName NVARCHAR(50) NOT NULL
);

-- User Table
CREATE TABLE dbo.[Users] (
    UserID INT PRIMARY KEY,
    RoleID INT FOREIGN KEY REFERENCES Role(RoleID),
    UserName NVARCHAR(100) NOT NULL,
    PasswordHash NVARCHAR(100) NOT NULL,
    FullName NVARCHAR(255),
    Email NVARCHAR(255),
    PhoneNumber NVARCHAR(20)
);

-- Vehicle Table
CREATE TABLE dbo.[Vehicle] (
    VehicleID INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    RegistrationNumber NVARCHAR(50) NOT NULL,
    Make NVARCHAR(50),
    Model NVARCHAR(50),
    Capacity INT
);

-- DeliveryStatus Table
CREATE TABLE dbo.[DeliveryStatus] (
    StatusID INT PRIMARY KEY,
    EstimatedArrivalTime DATETIME,
    ActualArrivalTime DATETIME,
    DepartedTime DATETIME,
    Status NVARCHAR(50)
);

-- Address Table
CREATE TABLE dbo.[Address] (
    AddressID INT PRIMARY KEY,
    Street NVARCHAR(255),
    City NVARCHAR(100),
    Province NVARCHAR(100),
    ZIPCode NVARCHAR(20),
    Country NVARCHAR(100)
);

-- Customer Table
CREATE TABLE dbo.[Customer] (
    CustomerID INT PRIMARY KEY,
    AddressID INT FOREIGN KEY REFERENCES Address(AddressID),
    Name NVARCHAR(100) NOT NULL,
    Phone NVARCHAR(20),
    Email NVARCHAR(255)
);

-- Order Table
CREATE TABLE dbo.[Order] (
    OrderID INT PRIMARY KEY,
    CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID),
    OrderDate DATETIME,
    OrderConfirmation NVARCHAR(100),
    OrderPrice DECIMAL(10, 2),
    Category NVARCHAR(50)
);

-- Payment Table
CREATE TABLE dbo.[Payment] (
    PaymentID INT PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES [Order](OrderID),
    PaymentStatus NVARCHAR(50),
    Amount DECIMAL(10, 2),
    PaymentDate DATETIME,
    PaymentMethod NVARCHAR(50)
);

-- Route Table
CREATE TABLE dbo.[Route] (
    RouteID INT PRIMARY KEY,
    Origin NVARCHAR(100) NOT NULL,
    Destination NVARCHAR(100) NOT NULL,
    Distance DECIMAL(10, 2)
);

-- Driver Table
CREATE TABLE dbo.[Driver] (
    DriverID INT PRIMARY KEY,
    RoleID INT FOREIGN KEY REFERENCES Role(RoleID),
    AddressID INT FOREIGN KEY REFERENCES Address(AddressID),
    DriverName NVARCHAR(100) NOT NULL,
    MobileNumber NVARCHAR(20),
    LicenseNumber NVARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- Assignment Table
CREATE TABLE dbo.[Assignment] (
    AssignmentID INT PRIMARY KEY,
    DriverID INT FOREIGN KEY REFERENCES Driver(DriverID),
    VehicleID INT FOREIGN KEY REFERENCES Vehicle(VehicleID)
);

-- Shipment Table
CREATE TABLE dbo.[Shipment] (
    ShipmentID INT PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES [Order](OrderID),
    RouteID INT FOREIGN KEY REFERENCES Route(RouteID),
    StatusID INT FOREIGN KEY REFERENCES DeliveryStatus(StatusID),
    CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID),
    AssignmentID INT FOREIGN KEY REFERENCES Assignment(AssignmentID)
);





