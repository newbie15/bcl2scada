Function GetProcessId(imageName, windowTitle)
    Dim currentUser, command, output, tasklist, tasks, i, cols

    currentUser = CreateObject("Wscript.Network").UserName

    command = "tasklist /V /FO csv"
    command = command & " /FI ""USERNAME eq " + currentUser + """"
    command = command & " /FI ""IMAGENAME eq " + imageName + """"
    command = command & " /FI ""WINDOWTITLE eq " + windowTitle + """"
    command = command & " /FI ""SESSIONNAME eq Console"""
    ' add more or different filters, see tasklist /?

    output = Trim(Shell(command))
    tasklist = Split(output, vbNewLine)

    ' starting at 1 skips first line (it contains the column headings only)
    For i = 1 To UBound(tasklist) - 1
        cols = Split(tasklist(i), """,""")
        ' a line is expected to have 9 columns (0-8)
        If UBound(cols) = 8 Then
            GetProcessId = Trim(cols(1))
            Exit For
        End If
    Next
End Function

Function Shell(cmd)
    Shell = WScript.CreateObject("WScript.Shell").Exec(cmd).StdOut.ReadAll()
End Function



dim y,pid0,pid1,pid2

Shell("C:\Python27\python-ku\Release\bcl2.exe")

do

    y = 0

    pid0 = GetProcessId("python.exe", "plc - Shortcut")
    If pid0 > 0 Then
        'MsgBox "Yay we found it"
        y = 1
    else
        pid1 = GetProcessId("python.exe", "C:\Python27\python.exe")
        If pid1 > 0 Then
            'MsgBox "Yay we found it"
            y = 1
        else
            pid2 = GetProcessId("python.exe", "C:\Windows\system32\cmd.exe - python  C:\Python27\python-ku\plc.py")
            If pid2 > 0 Then
                'MsgBox "Yay we found it"
                y = 1
            End If
        End If
    End If

    


    if y = 0 then
        ' msgbox "mulai"
        ' Set objShell = CreateObject("Shell.Application")
        ' objShell.ShellExecute "cscript", "python  C:\Python27\python-ku\plc.py", "", "runas", 1


        Set WshShell = WScript.CreateObject("WScript.Shell")
        Dim exeName
        Dim statusCode
        exeName = "python  C:\Python27\python-ku\plc.py"
        statusCode = WshShell.Run (exeName, 1, true)

    end if

    WScript.Sleep(60000)
loop
