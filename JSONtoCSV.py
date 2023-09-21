# Import necessary modules
import json
import csv
import os

# Define the path to the main folder
path = 'C:\\Users\\parih\\Desktop\\MalReport'

# Define a function to process the data in a JSON file
def converterFunc(jsonFilePath, csv_writer):
    try:
        # Open the JSON file and load its data
        print(f'Trying to open JSON data in {jsonFilePath}')
        with open(jsonFilePath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # Handle the error
        print(f'Error: Invalid JSON data in {jsonFilePath}')
        return []
    
    # Initializing "keys" list for storing WindowsAPI calls
    keys = ['CreateToolhelp32Snapshot', 'EnumDeviceDrivers', 'EnumProcesses', 'EnumProcessModules', 'EnumProcessModulesEx', 'FindFirstFileA', 'FindNextFileA', 'GetLogicalProcessorInformation', 'GetLogicalProcessorInformationEx', 'GetModuleBaseNameA', 'GetSystemDefaultLangId', 'GetVersionExA', 'GetWindowsDirectoryA', 'IsWoW64Process', 'Module32First', 'Module32Next', 'Process32First', 'Process32Next', 'ReadProcessMemory', 'Thread32First', 'Thread32Next', 'GetSystemDirectoryA', 'GetSystemTime', 'ReadFile', 'GetComputerNameA', 'VirtualQueryEx', 'GetProcessIdOfThread', 'GetProcessId', 'GetCurrentThread', 'GetCurrentThreadId', 'GetThreadId', 'GetThreadInformation', 'GetCurrentProcess', 'GetCurrentProcessId', 'SearchPathA', 'GetFileTime', 'GetFileAttributesA', 'LookupPrivilegeValueA', 'LookupAccountNameA', 'GetCurrentHwProfileA', 'GetUserNameA', 'RegEnumKeyExA', 'RegEnumValueA', 'RegQueryInfoKeyA', 'RegQueryMultipleValuesA', 'RegQueryValueExA', 'NtQueryDirectoryFile', 'NtQueryInformationProcess', 'NtQuerySystemEnvironmentValueEx', 'EnumDesktopWindows', 'EnumWindows', 'NetShareEnum', 'NetShareGetInfo', 'NetShareCheck', 'GetAdaptersInfo', 'PathFileExistsA', 'GetNativeSystemInfo', 'RtlGetVersion', 'GetIpNetTable', 'GetLogicalDrives', 'GetDriveTypeA', 'RegEnumKeyA', 'WNetEnumResourceA', 'WNetCloseEnum', 'FindFirstUrlCacheEntryA', 'FindNextUrlCacheEntryA', 'WNetAddConnection2A', 'WNetAddConnectionA', 'EnumResourceTypesA', 'EnumResourceTypesExA', 'GetSystemTimeAsFileTime', 'GetThreadLocale', 'EnumSystemLocalesA', 'CreateFileMappingA', 'CreateProcessA', 'CreateRemoteThread', 'CreateRemoteThreadEx', 'GetModuleHandleA', 'GetProcAddress', 'GetThreadContext', 'HeapCreate', 'LoadLibraryA', 'LoadLibraryExA', 'LocalAlloc', 'MapViewOfFile', 'MapViewOfFile2', 'MapViewOfFile3', 'MapViewOfFileEx', 'OpenThread', 'Process32First', 'Process32Next', 'QueueUserAPC', 'ReadProcessMemory', 'ResumeThread', 'SetProcessDEPPolicy', 'SetThreadContext', 'SuspendThread', 'Thread32First', 'Thread32Next', 'Toolhelp32ReadProcessMemory', 'VirtualAlloc', 'VirtualAllocEx', 'VirtualProtect', 'VirtualProtectEx', 'WriteProcessMemory', 'VirtualAllocExNuma', 'VirtualAlloc2', 'VirtualAlloc2FromApp', 'VirtualAllocFromApp', 'VirtualProtectFromApp', 'CreateThread', 'WaitForSingleObject', 'OpenProcess', 'OpenFileMappingA', 'GetProcessHeap', 'GetProcessHeaps', 'HeapAlloc', 'HeapReAlloc', 'GlobalAlloc', 'AdjustTokenPrivileges', 'CreateProcessAsUserA', 'OpenProcessToken', 'CreateProcessWithTokenW', 'NtAdjustPrivilegesToken', 'NtAllocateVirtualMemory', 'NtContinue', 'NtCreateProcess', 'NtCreateProcessEx', 'NtCreateSection', 'NtCreateThread', 'NtCreateThreadEx', 'NtCreateUserProcess', 'NtDuplicateObject', 'NtMapViewOfSection', 'NtOpenProcess', 'NtOpenThread', 'NtProtectVirtualMemory', 'NtQueueApcThread', 'NtQueueApcThreadEx', 'NtQueueApcThreadEx2', 'NtReadVirtualMemory', 'NtResumeThread', 'NtUnmapViewOfSection', 'NtWaitForMultipleObjects', 'NtWaitForSingleObject', 'NtWriteVirtualMemory', 'RtlCreateHeap', 'LdrLoadDll', 'RtlMoveMemory', 'RtlCopyMemory', 'SetPropA', 'WaitForSingleObjectEx', 'WaitForMultipleObjects', 'WaitForMultipleObjectsEx', 'KeInsertQueueApc', 'Wow64SetThreadContext', 'NtSuspendProcess', 'NtResumeProcess', 'DuplicateToken', 'NtReadVirtualMemoryEx', 'CreateProcessInternal', 'EnumSystemLocalesA', 'UuidFromStringA', 'CreateFileMappingA', 'DeleteFileA', 'GetModuleHandleA', 'GetProcAddress', 'LoadLibraryA', 'LoadLibraryExA', 'LoadResource', 'SetEnvironmentVariableA', 'SetFileTime', 'Sleep', 'WaitForSingleObject', 'SetFileAttributesA', 'SleepEx', 'NtDelayExecution', 'NtWaitForMultipleObjects', 'NtWaitForSingleObject', 'CreateWindowExA', 'RegisterHotKey', 'timeSetEvent', 'IcmpSendEcho', 'WaitForSingleObjectEx', 'WaitForMultipleObjects', 'WaitForMultipleObjectsEx', 'SetWaitableTimer', 'CreateTimerQueueTimer', 'CreateWaitableTimer', 'SetWaitableTimer', 'SetTimer', 'Select', 'ImpersonateLoggedOnUser', 'SetThreadToken', 'DuplicateToken', 'SizeOfResource', 'LockResource', 'CreateProcessInternal', 'TimeGetTime', 'EnumSystemLocalesA', 'UuidFromStringA', 'AttachThreadInput', 'CallNextHookEx', 'GetAsyncKeyState', 'GetClipboardData', 'GetDC', 'GetDCEx', 'GetForegroundWindow', 'GetKeyboardState', 'GetKeyState', 'GetMessageA', 'GetRawInputData', 'GetWindowDC', 'MapVirtualKeyA', 'MapVirtualKeyExA', 'PeekMessageA', 'PostMessageA', 'PostThreadMessageA', 'RegisterHotKey', 'RegisterRawInputDevices', 'SendMessageA', 'SendMessageCallbackA', 'SendMessageTimeoutA', 'SendNotifyMessageA', 'SetWindowsHookExA', 'SetWinEventHook', 'UnhookWindowsHookEx', 'BitBlt', 'StretchBlt', 'GetKeynameTextA', 'WinExec', 'FtpPutFileA', 'HttpOpenRequestA', 'HttpSendRequestA', 'HttpSendRequestExA', 'InternetCloseHandle', 'InternetOpenA', 'InternetOpenUrlA', 'InternetReadFile', 'InternetReadFileExA', 'InternetWriteFile', 'URLDownloadToFile', 'URLDownloadToCacheFile', 'URLOpenBlockingStream', 'URLOpenStream', 'Accept', 'Bind', 'Connect', 'Gethostbyname', 'Inet_addr', 'Recv', 'Send', 'WSAStartup', 'Gethostname', 'Socket', 'WSACleanup', 'Listen', 'ShellExecuteA', 'ShellExecuteExA', 'DnsQuery_A', 'DnsQueryEx', 'WNetOpenEnumA', 'FindFirstUrlCacheEntryA', 'FindNextUrlCacheEntryA', 'InternetConnectA', 'InternetSetOptionA', 'WSASocketA', 'Closesocket', 'WSAIoctl', 'ioctlsocket', 'HttpAddRequestHeaders', 'CreateToolhelp32Snapshot', 'GetLogicalProcessorInformation', 'GetLogicalProcessorInformationEx', 'GetTickCount', 'OutputDebugStringA', 'CheckRemoteDebuggerPresent', 'Sleep', 'GetSystemTime', 'GetComputerNameA', 'SleepEx', 'IsDebuggerPresent', 'GetUserNameA', 'NtQueryInformationProcess', 'ExitWindowsEx', 'FindWindowA', 'FindWindowExA', 'GetForegroundWindow', 'GetTickCount64', 'QueryPerformanceFrequency', 'QueryPerformanceCounter', 'GetNativeSystemInfo', 'RtlGetVersion', 'GetSystemTimeAsFileTime', 'CountClipboardFormats', 'CryptAcquireContextA', 'EncryptFileA', 'CryptEncrypt', 'CryptDecrypt', 'CryptCreateHash', 'CryptHashData', 'CryptDeriveKey', 'CryptSetKeyParam', 'CryptGetHashParam', 'CryptSetKeyParam', 'CryptDestroyKey', 'CryptGenRandom', 'DecryptFileA', 'FlushEfsCache', 'GetLogicalDrives', 'GetDriveTypeA', 'CryptStringToBinary', 'CryptBinaryToString', 'CryptReleaseContext', 'CryptDestroyHash', 'EnumSystemLocalesA', 'ConnectNamedPipe', 'CopyFileA', 'CreateFileA', 'CreateMutexA', 'CreateMutexExA', 'DeviceIoControl', 'FindResourceA', 'FindResourceExA', 'GetModuleBaseNameA', 'GetModuleFileNameA', 'GetModuleFileNameExA', 'GetTempPathA', 'IsWoW64Process', 'MoveFileA', 'MoveFileExA', 'PeekNamedPipe', 'WriteFile', 'TerminateThread', 'CopyFile2', 'CopyFileExA', 'CreateFile2', 'GetTempFileNameA', 'TerminateProcess', 'SetCurrentDirectory', 'FindClose', 'SetThreadPriority', 'UnmapViewOfFile', 'ControlService', 'ControlServiceExA', 'CreateServiceA', 'DeleteService', 'OpenSCManagerA', 'OpenServiceA', 'RegOpenKeyA', 'RegOpenKeyExA', 'StartServiceA', 'StartServiceCtrlDispatcherA', 'RegCreateKeyExA', 'RegCreateKeyA', 'RegSetValueExA', 'RegSetKeyValueA', 'RegDeleteValueA', 'RegOpenKeyExA', 'RegEnumKeyExA', 'RegEnumValueA', 'RegGetValueA', 'RegFlushKey', 'RegGetKeySecurity', 'RegLoadKeyA', 'RegLoadMUIStringA', 'RegOpenCurrentUser', 'RegOpenKeyTransactedA', 'RegOpenUserClassesRoot', 'RegOverridePredefKey', 'RegReplaceKeyA', 'RegRestoreKeyA', 'RegSaveKeyA', 'RegSaveKeyExA', 'RegSetKeySecurity', 'RegUnLoadKeyA', 'RegConnectRegistryA', 'RegCopyTreeA', 'RegCreateKeyTransactedA', 'RegDeleteKeyA', 'RegDeleteKeyExA', 'RegDeleteKeyTransactedA', 'RegDeleteKeyValueA', 'RegDeleteTreeA', 'RegDeleteValueA', 'RegCloseKey', 'NtClose', 'NtCreateFile', 'NtDeleteKey', 'NtDeleteValueKey', 'NtMakeTemporaryObject', 'NtSetContextThread', 'NtSetInformationProcess', 'NtSetInformationThread', 'NtSetSystemEnvironmentValueEx', 'NtSetValueKey', 'NtShutdownSystem', 'NtTerminateProcess', 'NtTerminateThread', 'RtlSetProcessIsCritical', 'DrawTextExA', 'GetDesktopWindow', 'SetClipboardData', 'SetWindowLongA', 'SetWindowLongPtrA', 'OpenClipboard', 'SetForegroundWindow', 'BringWindowToTop', 'SetFocus', 'ShowWindow', 'NetShareSetInfo', 'NetShareAdd', 'NtQueryTimer', 'GetIpNetTable', 'GetLogicalDrives', 'GetDriveTypeA', 'CreatePipe', 'RegEnumKeyA', 'WNetOpenEnumA', 'WNetEnumResourceA', 'WNetAddConnection2A', 'CallWindowProcA', 'NtResumeProcess', 'lstrcatA', 'ImpersonateLoggedOnUser', 'SetThreadToken', 'SizeOfResource', 'LockResource', 'UuidFromStringA']
    
    # Initializing "keysIndex" for storing the position of the API calls
    keysIndex = [x for x in range(len(keys))]
    
    # Initializing "keysDict" dictionary for merging the "keysIndex" and "keys" lists in the keys() and values() position respectively
    keysDict = dict(zip(keysIndex, keys))
    
    # Pre-initializing the "values" list with 0s and lenght similar to "keys" list
    value = [0]*len(keys)
    
    print("JSON data opened sucessfully")
    # Check if the "behavior" key is present in the data dictionary
    if "behavior" in data:
        print("Processing JSON data...")
        # Iterate over the elements in the data["behavior"] dictionary
        for i in data["behavior"]:
            # Check if the key is "apistats"
            if i == "apistats":
                # Iterate over the elements in the data["behavior"]["apistats"] dictionary
                for j in data["behavior"]["apistats"]:
                    for keyNumbers, keyValues in keysDict.items():
                        if keyValues in data["behavior"]["apistats"][j]:
                            # Set its value to 1 in the dictionary
                            value[keyNumbers] = 1
        
        print("JSON data processed sucessfully")
        
    else:
        # Write an error message to the CSV file
        print(f'Error: "behavior" key not found in {jsonFilePath}')
        return []
    
    # Return the list of extracted values
    return value

# Define a function to count the number of subfolders in a directory
def countSubFolders():
    # Count the number of items in the directory that are directories themselves
    ctr = len([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
    # Return the count
    return ctr

# Call the countSubFolders() function and store its return value in a variable named maxm
maxm = countSubFolders()

# Open a new CSV file named testdata.csv in write mode
with open('Maldata.csv', 'w', newline='') as f1:
    # Create a CSV writer object
    print(f'Opening {f1.name}')
    write = csv.writer(f1)
    print(f'Scanning through {path}')
    print(f'Total number of items:{maxm}')
    
    # Iterate over the range from 1 to maxm + 1 (inclusive)
    for i in range(1, maxm+1):
        # Construct the path to a subfolder by joining the path variable with the current loop index converted to a string
        subfolderPath = os.path.join(path, str(i))
        
        # Check if this subfolder exists
        if os.path.exists(subfolderPath):
            # Construct the path to a subfolder named reports inside this subfolder
            reportFolderPath = os.path.join(subfolderPath, 'reports')
            # Construct the path to a file named report.json inside this subfolder
            reportFilePath = os.path.join(reportFolderPath, 'report.json')
            
            # Check if this file exists
            if os.path.exists(reportFilePath):
                # Call the converterFunc() function with its path and csv_writer as arguments and store its return value in a variable named values
                print("Going to: %s" % reportFolderPath)
                values = converterFunc(reportFilePath, write)
                # Write these values to a row in the CSV file using the CSV writer object
                print(f'Copying data to {f1.name}\n')
                write.writerow(values)
    
    print("Task completed sucessfully!")
