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

extern int ncap_cap_DcFuncDerLoad(int, char*, char*, char**);
extern int ncap_cap_DcFuncLoad(int, char*, char*, char**);
extern int ncap_cap_TranFuncDerLoad(int, char*, char*, char**);
extern int ncap_cap_TranFuncLoad(int, char*, char*, char**);
extern int ncap_cap_NoiseLoadBiasDep(int, char*, char*, char**);

int ncap_cap_InstallDeviceBindings(struct ahdlDevDescData *desc) {

   ahdlBindDevDescFuncs(desc,
                        ncap_cap_DcFuncDerLoad,  
                        ncap_cap_DcFuncLoad,     
                        ncap_cap_TranFuncDerLoad,
                        ncap_cap_TranFuncLoad,   
                        ncap_cap_NoiseLoadBiasDep
                       );
   return 1; /** success **/
}
extern int ncap_cur_DcFuncDerLoad(int, char*, char*, char**);
extern int ncap_cur_DcFuncLoad(int, char*, char*, char**);
extern int ncap_cur_TranFuncDerLoad(int, char*, char*, char**);
extern int ncap_cur_TranFuncLoad(int, char*, char*, char**);
extern int ncap_cur_NoiseLoadBiasDep(int, char*, char*, char**);

int ncap_cur_InstallDeviceBindings(struct ahdlDevDescData *desc) {

   ahdlBindDevDescFuncs(desc,
                        ncap_cur_DcFuncDerLoad,  
                        ncap_cur_DcFuncLoad,     
                        ncap_cur_TranFuncDerLoad,
                        ncap_cur_TranFuncLoad,   
                        ncap_cur_NoiseLoadBiasDep
                       );
   return 1; /** success **/
}
extern int ncap_frcap_DcFuncDerLoad(int, char*, char*, char**);
extern int ncap_frcap_DcFuncLoad(int, char*, char*, char**);
extern int ncap_frcap_TranFuncDerLoad(int, char*, char*, char**);
extern int ncap_frcap_TranFuncLoad(int, char*, char*, char**);
extern int ncap_frcap_NoiseLoadBiasDep(int, char*, char*, char**);

int ncap_frcap_InstallDeviceBindings(struct ahdlDevDescData *desc) {

   ahdlBindDevDescFuncs(desc,
                        ncap_frcap_DcFuncDerLoad,  
                        ncap_frcap_DcFuncLoad,     
                        ncap_frcap_TranFuncDerLoad,
                        ncap_frcap_TranFuncLoad,   
                        ncap_frcap_NoiseLoadBiasDep
                       );
   return 1; /** success **/
}
extern int ncap_res1_DcFuncDerLoad(int, char*, char*, char**);
extern int ncap_res1_DcFuncLoad(int, char*, char*, char**);
extern int ncap_res1_TranFuncDerLoad(int, char*, char*, char**);
extern int ncap_res1_TranFuncLoad(int, char*, char*, char**);
extern int ncap_res1_NoiseLoadBiasDep(int, char*, char*, char**);

int ncap_res1_InstallDeviceBindings(struct ahdlDevDescData *desc) {

   ahdlBindDevDescFuncs(desc,
                        ncap_res1_DcFuncDerLoad,  
                        ncap_res1_DcFuncLoad,     
                        ncap_res1_TranFuncDerLoad,
                        ncap_res1_TranFuncLoad,   
                        ncap_res1_NoiseLoadBiasDep
                       );
   return 1; /** success **/
}
