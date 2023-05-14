
Set args = WScript.Arguments





aux_folder = args.Item(0)
script_folder = args.Item(1)
absolute_current_folder=args.Item(2)
script_name = args.Item(3)
batch_name = args.Item(4)



Set fileBatch = CreateObject("Scripting.FileSystemObject").CreateTextFile(absolute_current_folder & "\" & aux_folder & "\" & script_folder & "\" & batch_name, True)

fileBatch.WriteLine("@echo off")
fileBatch.WriteLine("python " & absolute_current_folder & "\" & aux_folder & "\" & script_folder & "\" & script_name & " %*")


fileBatch.Close