/***********************************************************************************
 ** Copyright (c) 2003 Cadence Design Systems, Inc. All rights reserved.          **
 **                                                                               **
 ** This work may not be copied, modified, re-published, uploaded, executed, or   **
 ** distributed in any way, in any medium, whether in whole or in part, without   **
 ** prior written permission from Cadence Design Systems, Inc.                    **
 **                                                                               **
 ** This file is automatically generated and will be overwritten. The interfaces  **
 ** used within this generated code are subject to change without notice.         **
 ***********************************************************************************/
#include "ahdlcmi.h"

int ahdlBsourceInterfaceVersion() {
   return 1; /* Only used when version >= spectre's BsourceInterfaceVersion */
}

extern int bsource_1_DcFuncDerLoad(int, char*, char*, char**);
extern int bsource_1_DcFuncLoad(int, char*, char*, char**);
extern int bsource_1_TranFuncDerLoad(int, char*, char*, char**);
extern int bsource_1_TranFuncLoad(int, char*, char*, char**);
extern int bsource_1_NoiseLoadBiasDep(int, char*, char*, char**);

int bsource_1_InstallDeviceBindings(struct ahdlDevDescData *desc) {

   ahdlBindDevDescFuncs(desc,
                        bsource_1_DcFuncDerLoad,  
                        bsource_1_DcFuncLoad,     
                        bsource_1_TranFuncDerLoad,
                        bsource_1_TranFuncLoad,   
                        bsource_1_NoiseLoadBiasDep
                       );
   return 1; /** success **/
}
extern int bsource_7_DcFuncDerLoad(int, char*, char*, char**);
extern int bsource_7_DcFuncLoad(int, char*, char*, char**);
extern int bsource_7_TranFuncDerLoad(int, char*, char*, char**);
extern int bsource_7_TranFuncLoad(int, char*, char*, char**);
extern int bsource_7_NoiseLoadBiasDep(int, char*, char*, char**);

int bsource_7_InstallDeviceBindings(struct ahdlDevDescData *desc) {

   ahdlBindDevDescFuncs(desc,
                        bsource_7_DcFuncDerLoad,  
                        bsource_7_DcFuncLoad,     
                        bsource_7_TranFuncDerLoad,
                        bsource_7_TranFuncLoad,   
                        bsource_7_NoiseLoadBiasDep
                       );
   return 1; /** success **/
}
