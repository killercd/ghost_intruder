Set objShell = WScript.CreateObject("WScript.Shell")
aux_folder = objShell.CurrentDirectory & "\aux_m\sshscan\"
new_path_env = Replace(objShell.Environment("System").Item("PATH"), aux_folder & ";", "")
new_path=new_path_env & aux_folder & ";"
objShell.Environment("System").Item("PATH") = new_path
WScript.Echo objShell.Environment("System").Item("PATH")
