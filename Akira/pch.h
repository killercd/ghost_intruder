// pch.h: This is a precompiled header file.
// Files listed below are compiled only once, improving build performance for future builds.
// This also affects IntelliSense performance, including code completion and many code browsing features.
// However, files listed here are ALL re-compiled if any one of them is updated between builds.
// Do not add files here that you will be updating frequently as this negates the performance advantage.

#ifndef PCH_H
#define PCH_H

// add headers that you want to pre-compile here
#define _CRT_SECURE_NO_WARNINGS
#include "framework.h"



#endif //PCH_H

//#include <windows.h>
//
//#include <winhttp.h>
//#include <stdio.h>
//#include <iostream>
//#include <string>
//#include <vector>
//#include <sstream>


#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <string>
#include <vector>

#pragma comment(lib, "Ws2_32.lib")

#define DEFAULT_BUFLEN 512
