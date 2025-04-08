@echo off
setlocal enabledelayedexpansion

:MENU
cls
title Secured Management Windows
echo ==========================================
echo         Secured Management Windows
echo ==========================================
echo.
echo Commands: type "colorset.(color)" to change colors
echo Available Colors: blue, green, red, hacker, default
echo ==========================================
echo.
echo 1  - Open Control Panel
echo 2  - Task Manager
echo 3  - System Properties
echo 4  - Command Prompt
echo 5  - File Explorer
echo 6  - System Information
echo 7  - Device Manager
echo 8  - Network Connections
echo 9  - Windows Update Settings
echo 10 - Programs and Features
echo 11 - Disk Management
echo 12 - Services
echo 13 - Registry Editor
echo 14 - Event Viewer
echo 15 - Power Options
echo 16 - User Accounts
echo 17 - Windows Firewall
echo 18 - Local Security Policy
echo 19 - Group Policy Editor
echo 20 - Exit
echo.
set /p choice=Choose an option or command: 

:: Color Changer
if /i "%choice%"=="colorset.blue" color 1F & goto MENU
if /i "%choice%"=="colorset.green" color 2F & goto MENU
if /i "%choice%"=="colorset.red" color 4F & goto MENU
if /i "%choice%"=="colorset.hacker" color 0A & goto MENU
if /i "%choice%"=="colorset.default" color 07 & goto MENU

:: Program Choices
if "%choice%"=="1" start control & goto MENU
if "%choice%"=="2" start taskmgr & goto MENU
if "%choice%"=="3" start sysdm.cpl & goto MENU
if "%choice%"=="4" start cmd & goto MENU
if "%choice%"=="5" start explorer & goto MENU
if "%choice%"=="6" start msinfo32 & goto MENU
if "%choice%"=="7" start devmgmt.msc & goto MENU
if "%choice%"=="8" start ncpa.cpl & goto MENU
if "%choice%"=="9" start ms-settings:windowsupdate & goto MENU
if "%choice%"=="10" start appwiz.cpl & goto MENU
if "%choice%"=="11" start diskmgmt.msc & goto MENU
if "%choice%"=="12" start services.msc & goto MENU
if "%choice%"=="13" start regedit & goto MENU
if "%choice%"=="14" start eventvwr & goto MENU
if "%choice%"=="15" start powercfg.cpl & goto MENU
if "%choice%"=="16" start control userpasswords2 & goto MENU
if "%choice%"=="17" start firewall.cpl & goto MENU
if "%choice%"=="18" start secpol.msc & goto MENU
if "%choice%"=="19" start gpedit.msc & goto MENU
if "%choice%"=="20" exit

echo Invalid Option or Command!
pause
goto MENU
