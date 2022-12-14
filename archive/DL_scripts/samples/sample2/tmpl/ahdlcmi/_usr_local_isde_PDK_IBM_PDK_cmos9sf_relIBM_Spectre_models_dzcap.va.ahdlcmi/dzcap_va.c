/** 1971803104 **/
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
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include "dzcap_va_inst_static.h"

static long   __BITWISE_LOGIC_OP_TEMP_VAR__;int dzcap_va_DcFuncDerLoad(int anal_mode, char* instData, char* modelData, char** stringList) {

int __msgSeverity__ = 0;
double	__tmpStkVar_2 = 0.0;
double	__tmpStkVar_1 = 0.0;


/*  Pre-Anal Load Code. */_I_Static_n_n1_1096 = 0.0;
_Static_d_by_dv_Rn1_928 = 0.0;
_I_Static_n1_n2_1112 = 0.0;
_Static_d_by_dv_Rn2_944 = 0.0;
_I_Static_n2_n3_1128 = 0.0;
_Static_d_by_dv_Rn3_960 = 0.0;
_I_Static_w1_p1_1192 = 0.0;
_Static_d_by_dv_Rp1_1024 = 0.0;
_I_Static_p1_p2_1208 = 0.0;
_Static_d_by_dv_Rp2_1040 = 0.0;
_I_Static_p2_p3_1224 = 0.0;
_Static_d_by_dv_Rp3_1056 = 0.0;
_I_Static_w1_p_1240 = 0.0;
_Static_d_by_dv_Rw_1072 = 0.0;
_I_Static_p2_sx_1256 = 0.0;
_Static_d_by_dv_diode_1088 = 0.0;

/*  C Code Every Code. */{ahdlDoSetLineNum ((long) 126);if (((_ntotal_80) > ((0L)))){ahdlDoSetLineNum ((long) 127);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = __INT_TO_DBL(_ntotal_80);(_nTrench_648) = __tempValueResultStatic;}}else{if ((__LOGIC_AND((((_l_88) <= ((0.00000000000000000000e+00)))), (((_w_112) <= ((0.00000000000000000000e+00))))))){ahdlDoSetLineNum ((long) 130);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = __INT_TO_DBL((((_nx_64) * (_ny_72))));(_nTrench_648) = __tempValueResultStatic;}}else{ahdlDoSetLineNum ((long) 134);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((((((((__FLOAT_DIV(((((_w_112) + (_tr_sp_232)))), (((((((_tr_w_208) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))) * (((((__FLOAT_DIV(((((_l_88) + (_tr_sp_232)))), (((((((_tr_l_184) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))))));(_nTrench_648) = __tempValueResultStatic;}}}ahdlDoSetLineNum ((long) 139);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((((((((((_nTrench_648) * (_tr_l_184)))) * (_tr_w_208)))) * (_tr_d_256))));(_area_688) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 141);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((__FLOAT_DIV((_Rn_spec_360), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));(_Rn_608) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 143);(_I_Static_n_n1_1096) += (__FLOAT_DIV(((getAcrossSolution2(_n_12, _n1_896))), ((_Rn_608))));_Static_d_by_dv_Rn1_928 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rn_608)))));ahdlDoSetLineNum ((long) 145);(_I_Static_n1_n2_1112) += (__FLOAT_DIV(((getAcrossSolution2(_n1_896, _n2_900))), ((_Rn_608))));_Static_d_by_dv_Rn2_944 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rn_608)))));ahdlDoSetLineNum ((long) 147);(_I_Static_n2_n3_1128) += (__FLOAT_DIV(((getAcrossSolution2(_n2_900, _n3_904))), ((_Rn_608))));_Static_d_by_dv_Rn3_960 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rn_608)))));ahdlDoSetLineNum ((long) 157);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((__FLOAT_DIV((_Rp_spec_384), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));(_Rp_568) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 159);(_I_Static_w1_p1_1192) += (__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p1_908))), ((_Rp_568))));_Static_d_by_dv_Rp1_1024 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rp_568)))));ahdlDoSetLineNum ((long) 161);(_I_Static_p1_p2_1208) += (__FLOAT_DIV(((getAcrossSolution2(_p1_908, _p2_912))), ((_Rp_568))));_Static_d_by_dv_Rp2_1040 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rp_568)))));ahdlDoSetLineNum ((long) 163);(_I_Static_p2_p3_1224) += (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _p3_916))), ((_Rp_568))));_Static_d_by_dv_Rp3_1056 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rp_568)))));ahdlDoSetLineNum ((long) 166);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((__FLOAT_DIV(((__FLOAT_DIV(((((_Rw_spec_408) * (_strap_l_136)))), (_strap_w_160)))), (_nTrench_648))));(_Rwell_528) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 168);(_I_Static_w1_p_1240) += ((((__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p_20))), ((_Rwell_528))))) * ((_nTrench_648))));_Static_d_by_dv_Rw_1072 += (((((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rwell_528)))))) * (((_nTrench_648)))));ahdlDoSetLineNum ((long) 171);(_I_Static_p2_sx_1256) += (((((((_js3_456)) * ((_area_688))))) * ((((LIMEXP(*(void **) (instData + 1080), (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _sx_28))), (((((_n_th_480)) * ((spectre_vt()))))))), &__tmpStkVar_1, &__tmpStkVar_2, &__tmpStkVar_2)) - __INT_TO_DBL((1L)))))));_Static_d_by_dv_diode_1088 += ((((((((_js3_456))) * (((_area_688)))))) * ((((((__FLOAT_DIV(((1.00000000000000000000e+00)), (((((_n_th_480))) * (((spectre_vt()))))))))) * ((__tmpStkVar_2)))))));}ahdlDoSetLineNum ((long) 173);   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n_12] -= _I_Static_n_n1_1096;
      ahdlStaticRHS[_n1_896] += _I_Static_n_n1_1096;
      ahdlStaticRHS_AbsSum[_n_12] += ABS(_I_Static_n_n1_1096);
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n_n1_1096);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 924),_Static_d_by_dv_Rn1_928);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n1_896] -= _I_Static_n1_n2_1112;
      ahdlStaticRHS[_n2_900] += _I_Static_n1_n2_1112;
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n1_n2_1112);
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n1_n2_1112);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 936),_Static_d_by_dv_Rn2_944);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n2_900] -= _I_Static_n2_n3_1128;
      ahdlStaticRHS[_n3_904] += _I_Static_n2_n3_1128;
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n2_n3_1128);
      ahdlStaticRHS_AbsSum[_n3_904] += ABS(_I_Static_n2_n3_1128);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 952),_Static_d_by_dv_Rn3_960);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p1_1192;
      ahdlStaticRHS[_p1_908] += _I_Static_w1_p1_1192;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p1_1192);
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_w1_p1_1192);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1016),_Static_d_by_dv_Rp1_1024);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p1_908] -= _I_Static_p1_p2_1208;
      ahdlStaticRHS[_p2_912] += _I_Static_p1_p2_1208;
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_p1_p2_1208);
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p1_p2_1208);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1032),_Static_d_by_dv_Rp2_1040);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_p3_1224;
      ahdlStaticRHS[_p3_916] += _I_Static_p2_p3_1224;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_p3_1224);
      ahdlStaticRHS_AbsSum[_p3_916] += ABS(_I_Static_p2_p3_1224);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1048),_Static_d_by_dv_Rp3_1056);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p_1240;
      ahdlStaticRHS[_p_20] += _I_Static_w1_p_1240;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p_1240);
      ahdlStaticRHS_AbsSum[_p_20] += ABS(_I_Static_w1_p_1240);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1064),_Static_d_by_dv_Rw_1072);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_sx_1256;
      ahdlStaticRHS[_sx_28] += _I_Static_p2_sx_1256;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_sx_1256);
      ahdlStaticRHS_AbsSum[_sx_28] += ABS(_I_Static_p2_sx_1256);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1084),_Static_d_by_dv_diode_1088);
    return __msgSeverity__;
} /** end of dzcap_va_DcFuncDerLoad **/

int dzcap_va_DcFuncLoad(int anal_mode, char* instData, char* modelData, char** stringList) {

int __msgSeverity__ = 0;
double	__tmpStkVar_2 = 0.0;
double	__tmpStkVar_1 = 0.0;


/*  Pre-Anal Load Code. */_I_Static_n_n1_1096 = 0.0;
_Static_d_by_dv_Rn1_928 = 0.0;
_I_Static_n1_n2_1112 = 0.0;
_Static_d_by_dv_Rn2_944 = 0.0;
_I_Static_n2_n3_1128 = 0.0;
_Static_d_by_dv_Rn3_960 = 0.0;
_I_Static_w1_p1_1192 = 0.0;
_Static_d_by_dv_Rp1_1024 = 0.0;
_I_Static_p1_p2_1208 = 0.0;
_Static_d_by_dv_Rp2_1040 = 0.0;
_I_Static_p2_p3_1224 = 0.0;
_Static_d_by_dv_Rp3_1056 = 0.0;
_I_Static_w1_p_1240 = 0.0;
_Static_d_by_dv_Rw_1072 = 0.0;
_I_Static_p2_sx_1256 = 0.0;
_Static_d_by_dv_diode_1088 = 0.0;

/*  C Code Every Code. */{ahdlDoSetLineNum ((long) 126);if (((_ntotal_80) > ((0L)))){ahdlDoSetLineNum ((long) 127);(_nTrench_648) = __INT_TO_DBL(_ntotal_80);}else{if ((__LOGIC_AND((((_l_88) <= ((0.00000000000000000000e+00)))), (((_w_112) <= ((0.00000000000000000000e+00))))))){ahdlDoSetLineNum ((long) 130);(_nTrench_648) = __INT_TO_DBL((((_nx_64) * (_ny_72))));}else{ahdlDoSetLineNum ((long) 134);(_nTrench_648) = ((((((((__FLOAT_DIV(((((_w_112) + (_tr_sp_232)))), (((((((_tr_w_208) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))) * (((((__FLOAT_DIV(((((_l_88) + (_tr_sp_232)))), (((((((_tr_l_184) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))))));}}ahdlDoSetLineNum ((long) 139);(_area_688) = ((((((((((_nTrench_648) * (_tr_l_184)))) * (_tr_w_208)))) * (_tr_d_256))));ahdlDoSetLineNum ((long) 141);(_Rn_608) = ((__FLOAT_DIV((_Rn_spec_360), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));ahdlDoSetLineNum ((long) 143);(_I_Static_n_n1_1096) += (__FLOAT_DIV(((getAcrossSolution2(_n_12, _n1_896))), ((_Rn_608))));ahdlDoSetLineNum ((long) 145);(_I_Static_n1_n2_1112) += (__FLOAT_DIV(((getAcrossSolution2(_n1_896, _n2_900))), ((_Rn_608))));ahdlDoSetLineNum ((long) 147);(_I_Static_n2_n3_1128) += (__FLOAT_DIV(((getAcrossSolution2(_n2_900, _n3_904))), ((_Rn_608))));ahdlDoSetLineNum ((long) 157);(_Rp_568) = ((__FLOAT_DIV((_Rp_spec_384), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));ahdlDoSetLineNum ((long) 159);(_I_Static_w1_p1_1192) += (__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p1_908))), ((_Rp_568))));ahdlDoSetLineNum ((long) 161);(_I_Static_p1_p2_1208) += (__FLOAT_DIV(((getAcrossSolution2(_p1_908, _p2_912))), ((_Rp_568))));ahdlDoSetLineNum ((long) 163);(_I_Static_p2_p3_1224) += (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _p3_916))), ((_Rp_568))));ahdlDoSetLineNum ((long) 166);(_Rwell_528) = ((__FLOAT_DIV(((__FLOAT_DIV(((((_Rw_spec_408) * (_strap_l_136)))), (_strap_w_160)))), (_nTrench_648))));ahdlDoSetLineNum ((long) 168);(_I_Static_w1_p_1240) += ((((__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p_20))), ((_Rwell_528))))) * ((_nTrench_648))));ahdlDoSetLineNum ((long) 171);(_I_Static_p2_sx_1256) += (((((((_js3_456)) * ((_area_688))))) * ((((LIMEXP(*(void **) (instData + 1080), (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _sx_28))), (((((_n_th_480)) * ((spectre_vt()))))))), &__tmpStkVar_1, &__tmpStkVar_2, &__tmpStkVar_2)) - __INT_TO_DBL((1L)))))));}ahdlDoSetLineNum ((long) 173);   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n_12] -= _I_Static_n_n1_1096;
      ahdlStaticRHS[_n1_896] += _I_Static_n_n1_1096;
      ahdlStaticRHS_AbsSum[_n_12] += ABS(_I_Static_n_n1_1096);
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n_n1_1096);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n1_896] -= _I_Static_n1_n2_1112;
      ahdlStaticRHS[_n2_900] += _I_Static_n1_n2_1112;
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n1_n2_1112);
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n1_n2_1112);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n2_900] -= _I_Static_n2_n3_1128;
      ahdlStaticRHS[_n3_904] += _I_Static_n2_n3_1128;
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n2_n3_1128);
      ahdlStaticRHS_AbsSum[_n3_904] += ABS(_I_Static_n2_n3_1128);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p1_1192;
      ahdlStaticRHS[_p1_908] += _I_Static_w1_p1_1192;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p1_1192);
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_w1_p1_1192);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p1_908] -= _I_Static_p1_p2_1208;
      ahdlStaticRHS[_p2_912] += _I_Static_p1_p2_1208;
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_p1_p2_1208);
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p1_p2_1208);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_p3_1224;
      ahdlStaticRHS[_p3_916] += _I_Static_p2_p3_1224;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_p3_1224);
      ahdlStaticRHS_AbsSum[_p3_916] += ABS(_I_Static_p2_p3_1224);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p_1240;
      ahdlStaticRHS[_p_20] += _I_Static_w1_p_1240;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p_1240);
      ahdlStaticRHS_AbsSum[_p_20] += ABS(_I_Static_w1_p_1240);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_sx_1256;
      ahdlStaticRHS[_sx_28] += _I_Static_p2_sx_1256;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_sx_1256);
      ahdlStaticRHS_AbsSum[_sx_28] += ABS(_I_Static_p2_sx_1256);
   }

    return __msgSeverity__;
} /** end of dzcap_va_DcFuncLoad **/

int dzcap_va_TranFuncDerLoad(int anal_mode, char* instData, char* modelData, char** stringList) {

int __msgSeverity__ = 0;
double	__tmpStkVar_2 = 0.0;
double	__tmpStkVar_1 = 0.0;


/*  Pre-Anal Load Code. */_I_Static_n_n1_1096 = 0.0;
_Static_d_by_dv_Rn1_928 = 0.0;
_I_Static_n1_n2_1112 = 0.0;
_Static_d_by_dv_Rn2_944 = 0.0;
_I_Static_n2_n3_1128 = 0.0;
_Static_d_by_dv_Rn3_960 = 0.0;
_I_Dynamic_n1_p1_1152 = 0.0;
_Dynamic_d_by_dv_C1_976 = 0.0;
_I_Dynamic_n2_p2_1168 = 0.0;
_Dynamic_d_by_dv_C2_992 = 0.0;
_I_Dynamic_n3_p3_1184 = 0.0;
_Dynamic_d_by_dv_C3_1008 = 0.0;
_I_Static_w1_p1_1192 = 0.0;
_Static_d_by_dv_Rp1_1024 = 0.0;
_I_Static_p1_p2_1208 = 0.0;
_Static_d_by_dv_Rp2_1040 = 0.0;
_I_Static_p2_p3_1224 = 0.0;
_Static_d_by_dv_Rp3_1056 = 0.0;
_I_Static_w1_p_1240 = 0.0;
_Static_d_by_dv_Rw_1072 = 0.0;
_I_Static_p2_sx_1256 = 0.0;
_Static_d_by_dv_diode_1088 = 0.0;

/*  C Code Every Code. */{ahdlDoSetLineNum ((long) 126);if (((_ntotal_80) > ((0L)))){ahdlDoSetLineNum ((long) 127);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = __INT_TO_DBL(_ntotal_80);(_nTrench_648) = __tempValueResultStatic;}}else{if ((__LOGIC_AND((((_l_88) <= ((0.00000000000000000000e+00)))), (((_w_112) <= ((0.00000000000000000000e+00))))))){ahdlDoSetLineNum ((long) 130);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = __INT_TO_DBL((((_nx_64) * (_ny_72))));(_nTrench_648) = __tempValueResultStatic;}}else{ahdlDoSetLineNum ((long) 134);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((((((((__FLOAT_DIV(((((_w_112) + (_tr_sp_232)))), (((((((_tr_w_208) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))) * (((((__FLOAT_DIV(((((_l_88) + (_tr_sp_232)))), (((((((_tr_l_184) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))))));(_nTrench_648) = __tempValueResultStatic;}}}ahdlDoSetLineNum ((long) 139);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((((((((((_nTrench_648) * (_tr_l_184)))) * (_tr_w_208)))) * (_tr_d_256))));(_area_688) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 141);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((__FLOAT_DIV((_Rn_spec_360), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));(_Rn_608) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 143);(_I_Static_n_n1_1096) += (__FLOAT_DIV(((getAcrossSolution2(_n_12, _n1_896))), ((_Rn_608))));_Static_d_by_dv_Rn1_928 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rn_608)))));ahdlDoSetLineNum ((long) 145);(_I_Static_n1_n2_1112) += (__FLOAT_DIV(((getAcrossSolution2(_n1_896, _n2_900))), ((_Rn_608))));_Static_d_by_dv_Rn2_944 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rn_608)))));ahdlDoSetLineNum ((long) 147);(_I_Static_n2_n3_1128) += (__FLOAT_DIV(((getAcrossSolution2(_n2_900, _n3_904))), ((_Rn_608))));_Static_d_by_dv_Rn3_960 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rn_608)))));ahdlDoSetLineNum ((long) 151);(_I_Dynamic_n1_p1_1152) += (__FLOAT_DIV((((((((((((_C_spec_336)) * ((getAcrossSolution2(_n1_896, _p1_908)))))) * ((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304)))))))) * ((_nTrench_648))))), __INT_TO_DBL((_nSegments_324))));_Dynamic_d_by_dv_C1_976 += ((__FLOAT_DIV(((((((((_C_spec_336))) * (((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304))))))))) * (((_nTrench_648))))), __INT_TO_DBL((_nSegments_324)))));ahdlDoSetLineNum ((long) 153);(_I_Dynamic_n2_p2_1168) += (__FLOAT_DIV((((((((((((_C_spec_336)) * ((getAcrossSolution2(_n2_900, _p2_912)))))) * ((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304)))))))) * ((_nTrench_648))))), __INT_TO_DBL((_nSegments_324))));_Dynamic_d_by_dv_C2_992 += ((__FLOAT_DIV(((((((((_C_spec_336))) * (((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304))))))))) * (((_nTrench_648))))), __INT_TO_DBL((_nSegments_324)))));ahdlDoSetLineNum ((long) 155);(_I_Dynamic_n3_p3_1184) += (__FLOAT_DIV((((((((((((_C_spec_336)) * ((getAcrossSolution2(_n3_904, _p3_916)))))) * ((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304)))))))) * ((_nTrench_648))))), __INT_TO_DBL((_nSegments_324))));_Dynamic_d_by_dv_C3_1008 += ((__FLOAT_DIV(((((((((_C_spec_336))) * (((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304))))))))) * (((_nTrench_648))))), __INT_TO_DBL((_nSegments_324)))));ahdlDoSetLineNum ((long) 157);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((__FLOAT_DIV((_Rp_spec_384), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));(_Rp_568) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 159);(_I_Static_w1_p1_1192) += (__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p1_908))), ((_Rp_568))));_Static_d_by_dv_Rp1_1024 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rp_568)))));ahdlDoSetLineNum ((long) 161);(_I_Static_p1_p2_1208) += (__FLOAT_DIV(((getAcrossSolution2(_p1_908, _p2_912))), ((_Rp_568))));_Static_d_by_dv_Rp2_1040 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rp_568)))));ahdlDoSetLineNum ((long) 163);(_I_Static_p2_p3_1224) += (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _p3_916))), ((_Rp_568))));_Static_d_by_dv_Rp3_1056 += ((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rp_568)))));ahdlDoSetLineNum ((long) 166);{double __tempValueResultStatic;double __tempValueResultDynamic;
__tempValueResultStatic = ((__FLOAT_DIV(((__FLOAT_DIV(((((_Rw_spec_408) * (_strap_l_136)))), (_strap_w_160)))), (_nTrench_648))));(_Rwell_528) = __tempValueResultStatic;}ahdlDoSetLineNum ((long) 168);(_I_Static_w1_p_1240) += ((((__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p_20))), ((_Rwell_528))))) * ((_nTrench_648))));_Static_d_by_dv_Rw_1072 += (((((__FLOAT_DIV(((1.00000000000000000000e+00)), ((_Rwell_528)))))) * (((_nTrench_648)))));ahdlDoSetLineNum ((long) 171);(_I_Static_p2_sx_1256) += (((((((_js3_456)) * ((_area_688))))) * ((((LIMEXP(*(void **) (instData + 1080), (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _sx_28))), (((((_n_th_480)) * ((spectre_vt()))))))), &__tmpStkVar_1, &__tmpStkVar_2, &__tmpStkVar_2)) - __INT_TO_DBL((1L)))))));_Static_d_by_dv_diode_1088 += ((((((((_js3_456))) * (((_area_688)))))) * ((((((__FLOAT_DIV(((1.00000000000000000000e+00)), (((((_n_th_480))) * (((spectre_vt()))))))))) * ((__tmpStkVar_2)))))));}ahdlDoSetLineNum ((long) 173);   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n_12] -= _I_Static_n_n1_1096;
      ahdlStaticRHS[_n1_896] += _I_Static_n_n1_1096;
      ahdlStaticRHS_AbsSum[_n_12] += ABS(_I_Static_n_n1_1096);
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n_n1_1096);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 924),_Static_d_by_dv_Rn1_928);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n1_896] -= _I_Static_n1_n2_1112;
      ahdlStaticRHS[_n2_900] += _I_Static_n1_n2_1112;
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n1_n2_1112);
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n1_n2_1112);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 936),_Static_d_by_dv_Rn2_944);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n2_900] -= _I_Static_n2_n3_1128;
      ahdlStaticRHS[_n3_904] += _I_Static_n2_n3_1128;
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n2_n3_1128);
      ahdlStaticRHS_AbsSum[_n3_904] += ABS(_I_Static_n2_n3_1128);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 952),_Static_d_by_dv_Rn3_960);
   if (ahdlWhatsNeeded IS devDynamicFuncNeeded) {
      ahdlDynamicRHS[_n1_896] -= _I_Dynamic_n1_p1_1152;
      ahdlDynamicRHS[_p1_908] += _I_Dynamic_n1_p1_1152;
      ahdlDynamicRHS_AbsSum[_n1_896] += ABS(_I_Dynamic_n1_p1_1152);
      ahdlDynamicRHS_AbsSum[_p1_908] += ABS(_I_Dynamic_n1_p1_1152);
   }

      ahdlInterAddDynamicQuartet(*(void**)(instData + 968),_Dynamic_d_by_dv_C1_976);
   if (ahdlWhatsNeeded IS devDynamicFuncNeeded) {
      ahdlDynamicRHS[_n2_900] -= _I_Dynamic_n2_p2_1168;
      ahdlDynamicRHS[_p2_912] += _I_Dynamic_n2_p2_1168;
      ahdlDynamicRHS_AbsSum[_n2_900] += ABS(_I_Dynamic_n2_p2_1168);
      ahdlDynamicRHS_AbsSum[_p2_912] += ABS(_I_Dynamic_n2_p2_1168);
   }

      ahdlInterAddDynamicQuartet(*(void**)(instData + 984),_Dynamic_d_by_dv_C2_992);
   if (ahdlWhatsNeeded IS devDynamicFuncNeeded) {
      ahdlDynamicRHS[_n3_904] -= _I_Dynamic_n3_p3_1184;
      ahdlDynamicRHS[_p3_916] += _I_Dynamic_n3_p3_1184;
      ahdlDynamicRHS_AbsSum[_n3_904] += ABS(_I_Dynamic_n3_p3_1184);
      ahdlDynamicRHS_AbsSum[_p3_916] += ABS(_I_Dynamic_n3_p3_1184);
   }

      ahdlInterAddDynamicQuartet(*(void**)(instData + 1000),_Dynamic_d_by_dv_C3_1008);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p1_1192;
      ahdlStaticRHS[_p1_908] += _I_Static_w1_p1_1192;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p1_1192);
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_w1_p1_1192);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1016),_Static_d_by_dv_Rp1_1024);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p1_908] -= _I_Static_p1_p2_1208;
      ahdlStaticRHS[_p2_912] += _I_Static_p1_p2_1208;
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_p1_p2_1208);
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p1_p2_1208);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1032),_Static_d_by_dv_Rp2_1040);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_p3_1224;
      ahdlStaticRHS[_p3_916] += _I_Static_p2_p3_1224;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_p3_1224);
      ahdlStaticRHS_AbsSum[_p3_916] += ABS(_I_Static_p2_p3_1224);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1048),_Static_d_by_dv_Rp3_1056);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p_1240;
      ahdlStaticRHS[_p_20] += _I_Static_w1_p_1240;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p_1240);
      ahdlStaticRHS_AbsSum[_p_20] += ABS(_I_Static_w1_p_1240);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1064),_Static_d_by_dv_Rw_1072);
   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_sx_1256;
      ahdlStaticRHS[_sx_28] += _I_Static_p2_sx_1256;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_sx_1256);
      ahdlStaticRHS_AbsSum[_sx_28] += ABS(_I_Static_p2_sx_1256);
   }

      ahdlInterAddStaticQuartet(*(void**)(instData + 1084),_Static_d_by_dv_diode_1088);
    return __msgSeverity__;
} /** end of dzcap_va_TranFuncDerLoad **/

int dzcap_va_TranFuncLoad(int anal_mode, char* instData, char* modelData, char** stringList) {

int __msgSeverity__ = 0;
double	__tmpStkVar_2 = 0.0;
double	__tmpStkVar_1 = 0.0;


/*  Pre-Anal Load Code. */_I_Static_n_n1_1096 = 0.0;
_Static_d_by_dv_Rn1_928 = 0.0;
_I_Static_n1_n2_1112 = 0.0;
_Static_d_by_dv_Rn2_944 = 0.0;
_I_Static_n2_n3_1128 = 0.0;
_Static_d_by_dv_Rn3_960 = 0.0;
_I_Dynamic_n1_p1_1152 = 0.0;
_Dynamic_d_by_dv_C1_976 = 0.0;
_I_Dynamic_n2_p2_1168 = 0.0;
_Dynamic_d_by_dv_C2_992 = 0.0;
_I_Dynamic_n3_p3_1184 = 0.0;
_Dynamic_d_by_dv_C3_1008 = 0.0;
_I_Static_w1_p1_1192 = 0.0;
_Static_d_by_dv_Rp1_1024 = 0.0;
_I_Static_p1_p2_1208 = 0.0;
_Static_d_by_dv_Rp2_1040 = 0.0;
_I_Static_p2_p3_1224 = 0.0;
_Static_d_by_dv_Rp3_1056 = 0.0;
_I_Static_w1_p_1240 = 0.0;
_Static_d_by_dv_Rw_1072 = 0.0;
_I_Static_p2_sx_1256 = 0.0;
_Static_d_by_dv_diode_1088 = 0.0;

/*  C Code Every Code. */{ahdlDoSetLineNum ((long) 126);if (((_ntotal_80) > ((0L)))){ahdlDoSetLineNum ((long) 127);(_nTrench_648) = __INT_TO_DBL(_ntotal_80);}else{if ((__LOGIC_AND((((_l_88) <= ((0.00000000000000000000e+00)))), (((_w_112) <= ((0.00000000000000000000e+00))))))){ahdlDoSetLineNum ((long) 130);(_nTrench_648) = __INT_TO_DBL((((_nx_64) * (_ny_72))));}else{ahdlDoSetLineNum ((long) 134);(_nTrench_648) = ((((((((__FLOAT_DIV(((((_w_112) + (_tr_sp_232)))), (((((((_tr_w_208) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))) * (((((__FLOAT_DIV(((((_l_88) + (_tr_sp_232)))), (((((((_tr_l_184) + (_tr_sp_232)))) + ((1.00000000000000249509e-24)))))))) - (((__INT_TO_DBL((2L)) * (_nDummy_432))))))))));}}ahdlDoSetLineNum ((long) 139);(_area_688) = ((((((((((_nTrench_648) * (_tr_l_184)))) * (_tr_w_208)))) * (_tr_d_256))));ahdlDoSetLineNum ((long) 141);(_Rn_608) = ((__FLOAT_DIV((_Rn_spec_360), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));ahdlDoSetLineNum ((long) 143);(_I_Static_n_n1_1096) += (__FLOAT_DIV(((getAcrossSolution2(_n_12, _n1_896))), ((_Rn_608))));ahdlDoSetLineNum ((long) 145);(_I_Static_n1_n2_1112) += (__FLOAT_DIV(((getAcrossSolution2(_n1_896, _n2_900))), ((_Rn_608))));ahdlDoSetLineNum ((long) 147);(_I_Static_n2_n3_1128) += (__FLOAT_DIV(((getAcrossSolution2(_n2_900, _n3_904))), ((_Rn_608))));ahdlDoSetLineNum ((long) 151);(_I_Dynamic_n1_p1_1152) += (__FLOAT_DIV((((((((((((_C_spec_336)) * ((getAcrossSolution2(_n1_896, _p1_908)))))) * ((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304)))))))) * ((_nTrench_648))))), __INT_TO_DBL((_nSegments_324))));ahdlDoSetLineNum ((long) 153);(_I_Dynamic_n2_p2_1168) += (__FLOAT_DIV((((((((((((_C_spec_336)) * ((getAcrossSolution2(_n2_900, _p2_912)))))) * ((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304)))))))) * ((_nTrench_648))))), __INT_TO_DBL((_nSegments_324))));ahdlDoSetLineNum ((long) 155);(_I_Dynamic_n3_p3_1184) += (__FLOAT_DIV((((((((((((_C_spec_336)) * ((getAcrossSolution2(_n3_904, _p3_916)))))) * ((__FLOAT_DIV(((_dz_tox_n_280)), ((_dz_tox_f_304)))))))) * ((_nTrench_648))))), __INT_TO_DBL((_nSegments_324))));ahdlDoSetLineNum ((long) 157);(_Rp_568) = ((__FLOAT_DIV((_Rp_spec_384), ((((_nTrench_648) * __INT_TO_DBL(_nSegments_324)))))));ahdlDoSetLineNum ((long) 159);(_I_Static_w1_p1_1192) += (__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p1_908))), ((_Rp_568))));ahdlDoSetLineNum ((long) 161);(_I_Static_p1_p2_1208) += (__FLOAT_DIV(((getAcrossSolution2(_p1_908, _p2_912))), ((_Rp_568))));ahdlDoSetLineNum ((long) 163);(_I_Static_p2_p3_1224) += (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _p3_916))), ((_Rp_568))));ahdlDoSetLineNum ((long) 166);(_Rwell_528) = ((__FLOAT_DIV(((__FLOAT_DIV(((((_Rw_spec_408) * (_strap_l_136)))), (_strap_w_160)))), (_nTrench_648))));ahdlDoSetLineNum ((long) 168);(_I_Static_w1_p_1240) += ((((__FLOAT_DIV(((getAcrossSolution2(_w1_920, _p_20))), ((_Rwell_528))))) * ((_nTrench_648))));ahdlDoSetLineNum ((long) 171);(_I_Static_p2_sx_1256) += (((((((_js3_456)) * ((_area_688))))) * ((((LIMEXP(*(void **) (instData + 1080), (__FLOAT_DIV(((getAcrossSolution2(_p2_912, _sx_28))), (((((_n_th_480)) * ((spectre_vt()))))))), &__tmpStkVar_1, &__tmpStkVar_2, &__tmpStkVar_2)) - __INT_TO_DBL((1L)))))));}ahdlDoSetLineNum ((long) 173);   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n_12] -= _I_Static_n_n1_1096;
      ahdlStaticRHS[_n1_896] += _I_Static_n_n1_1096;
      ahdlStaticRHS_AbsSum[_n_12] += ABS(_I_Static_n_n1_1096);
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n_n1_1096);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n1_896] -= _I_Static_n1_n2_1112;
      ahdlStaticRHS[_n2_900] += _I_Static_n1_n2_1112;
      ahdlStaticRHS_AbsSum[_n1_896] += ABS(_I_Static_n1_n2_1112);
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n1_n2_1112);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_n2_900] -= _I_Static_n2_n3_1128;
      ahdlStaticRHS[_n3_904] += _I_Static_n2_n3_1128;
      ahdlStaticRHS_AbsSum[_n2_900] += ABS(_I_Static_n2_n3_1128);
      ahdlStaticRHS_AbsSum[_n3_904] += ABS(_I_Static_n2_n3_1128);
   }

   if (ahdlWhatsNeeded IS devDynamicFuncNeeded) {
      ahdlDynamicRHS[_n1_896] -= _I_Dynamic_n1_p1_1152;
      ahdlDynamicRHS[_p1_908] += _I_Dynamic_n1_p1_1152;
      ahdlDynamicRHS_AbsSum[_n1_896] += ABS(_I_Dynamic_n1_p1_1152);
      ahdlDynamicRHS_AbsSum[_p1_908] += ABS(_I_Dynamic_n1_p1_1152);
   }

   if (ahdlWhatsNeeded IS devDynamicFuncNeeded) {
      ahdlDynamicRHS[_n2_900] -= _I_Dynamic_n2_p2_1168;
      ahdlDynamicRHS[_p2_912] += _I_Dynamic_n2_p2_1168;
      ahdlDynamicRHS_AbsSum[_n2_900] += ABS(_I_Dynamic_n2_p2_1168);
      ahdlDynamicRHS_AbsSum[_p2_912] += ABS(_I_Dynamic_n2_p2_1168);
   }

   if (ahdlWhatsNeeded IS devDynamicFuncNeeded) {
      ahdlDynamicRHS[_n3_904] -= _I_Dynamic_n3_p3_1184;
      ahdlDynamicRHS[_p3_916] += _I_Dynamic_n3_p3_1184;
      ahdlDynamicRHS_AbsSum[_n3_904] += ABS(_I_Dynamic_n3_p3_1184);
      ahdlDynamicRHS_AbsSum[_p3_916] += ABS(_I_Dynamic_n3_p3_1184);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p1_1192;
      ahdlStaticRHS[_p1_908] += _I_Static_w1_p1_1192;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p1_1192);
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_w1_p1_1192);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p1_908] -= _I_Static_p1_p2_1208;
      ahdlStaticRHS[_p2_912] += _I_Static_p1_p2_1208;
      ahdlStaticRHS_AbsSum[_p1_908] += ABS(_I_Static_p1_p2_1208);
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p1_p2_1208);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_p3_1224;
      ahdlStaticRHS[_p3_916] += _I_Static_p2_p3_1224;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_p3_1224);
      ahdlStaticRHS_AbsSum[_p3_916] += ABS(_I_Static_p2_p3_1224);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_w1_920] -= _I_Static_w1_p_1240;
      ahdlStaticRHS[_p_20] += _I_Static_w1_p_1240;
      ahdlStaticRHS_AbsSum[_w1_920] += ABS(_I_Static_w1_p_1240);
      ahdlStaticRHS_AbsSum[_p_20] += ABS(_I_Static_w1_p_1240);
   }

   if (ahdlWhatsNeeded IS devStaticFuncNeeded) {
      ahdlStaticRHS[_p2_912] -= _I_Static_p2_sx_1256;
      ahdlStaticRHS[_sx_28] += _I_Static_p2_sx_1256;
      ahdlStaticRHS_AbsSum[_p2_912] += ABS(_I_Static_p2_sx_1256);
      ahdlStaticRHS_AbsSum[_sx_28] += ABS(_I_Static_p2_sx_1256);
   }

    return __msgSeverity__;
} /** end of dzcap_va_TranFuncLoad **/

int dzcap_va_NoiseLoadBiasDep(int anal_mode, char* instData, char* modelData, char** stringList) {

int __msgSeverity__ = 0;
double	__tmpStkVar_2 = 0.0;
double	__tmpStkVar_1 = 0.0;


    return __msgSeverity__;
} /** end of dzcap_va_NoiseLoadBiasDep **/

