# Relazione Analisi Predittiva: Salary Dataset

## 1. Metriche di Confidenza del Modello
Modello di Regressione Lineare addestrato sul subset degli studenti inseriti (`placed == 1`).

| Metrica | Valore |
| :--- | :--- |
| R-squared | 1.0000 |
| Mean Absolute Error (MAE) | 0.0000 |
| Root Mean Squared Error (RMSE) | 0.0000 |

## 2. Analisi dei Coefficienti
Valori dei coefficienti del modello di regressione, paginati per chiarezza di lettura.

### Blocco 1 (Feature 1 - 10)
| Feature             |   Coefficiente |
|:--------------------|---------------:|
| cgpa                |      0.780736  |
| college_tier        |      0.677465  |
| python_skill        |      0.396659  |
| dsa_skill           |      0.0995002 |
| ml_skill            |      1.39066   |
| web_dev_skill       |      1.73449   |
| coding_score        |      0.0789601 |
| communication_score |      1.6855    |
| aptitude_score      |     -0.0403038 |
| internships         |      3.98028   |

---

### Blocco 2 (Feature 11 - 20)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| projects         |       1.39474  |
| backlogs         |       0.429708 |
| resume_score     |      -0.224101 |
| skill_score      |       3.62131  |
| student_id_S1    |       3.22948  |
| student_id_S10   |      -2.02304  |
| student_id_S100  |       1.06977  |
| student_id_S1000 |       3.9087   |
| student_id_S1001 |      -8.00661  |
| student_id_S1003 |      14.2434   |

---

### Blocco 3 (Feature 21 - 30)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1004 |      8.835     |
| student_id_S1005 |      1.41346   |
| student_id_S1007 |      0.911046  |
| student_id_S1008 |    -10.6805    |
| student_id_S1009 |     -0.0475337 |
| student_id_S101  |     -3.0313    |
| student_id_S1011 |      3.04879   |
| student_id_S1012 |      3.55098   |
| student_id_S1013 |     -1.57048   |
| student_id_S1014 |      4.12637   |

---

### Blocco 4 (Feature 31 - 40)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1016 |       6.306    |
| student_id_S1017 |      11.2594   |
| student_id_S1018 |       0.958841 |
| student_id_S102  |       3.37614  |
| student_id_S1020 |       7.63429  |
| student_id_S1022 |      11.19     |
| student_id_S1023 |      -5.30323  |
| student_id_S1024 |      -3.04329  |
| student_id_S1026 |       5.3097   |
| student_id_S1027 |      10.7202   |

---

### Blocco 5 (Feature 41 - 50)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1028 |      -9.17735  |
| student_id_S103  |       0.151674 |
| student_id_S1030 |     -10.0632   |
| student_id_S1031 |      -9.96169  |
| student_id_S1032 |       9.07575  |
| student_id_S1033 |      -8.18739  |
| student_id_S1034 |      -0.961849 |
| student_id_S1035 |      -6.1442   |
| student_id_S1036 |      -1.03295  |
| student_id_S1037 |       7.63134  |

---

### Blocco 6 (Feature 51 - 60)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1038 |    -10.4553    |
| student_id_S1039 |     16.2136    |
| student_id_S1040 |     -6.85787   |
| student_id_S1041 |     12.2293    |
| student_id_S1042 |     -6.35386   |
| student_id_S1043 |     16.9757    |
| student_id_S1045 |      0.0426834 |
| student_id_S1046 |     -0.738424  |
| student_id_S1047 |     -1.16555   |
| student_id_S1048 |     -2.87103   |

---

### Blocco 7 (Feature 61 - 70)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1049 |       0.818786 |
| student_id_S1050 |       4.59842  |
| student_id_S1051 |      -0.497333 |
| student_id_S1052 |       1.95819  |
| student_id_S1054 |       5.58293  |
| student_id_S1055 |      -6.08163  |
| student_id_S1056 |      -4.85693  |
| student_id_S1058 |      10.8365   |
| student_id_S106  |      -4.02437  |
| student_id_S1062 |       7.68055  |

---

### Blocco 8 (Feature 71 - 80)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1063 |    -4.46434    |
| student_id_S1064 |     0.00999824 |
| student_id_S1065 |    -0.880938   |
| student_id_S1066 |    -6.09625    |
| student_id_S1067 |    -8.17614    |
| student_id_S1068 |     4.5039     |
| student_id_S1069 |    -0.0561579  |
| student_id_S107  |    -2.15992    |
| student_id_S1070 |     1.63525    |
| student_id_S1071 |    16.1857     |

---

### Blocco 9 (Feature 81 - 90)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1073 |       -4.62419 |
| student_id_S1074 |       -8.65709 |
| student_id_S1075 |        6.83503 |
| student_id_S1076 |        6.06506 |
| student_id_S1077 |       -9.22673 |
| student_id_S1078 |       -5.89643 |
| student_id_S1079 |       -6.57624 |
| student_id_S108  |       -1.60557 |
| student_id_S1080 |        9.05612 |
| student_id_S1081 |        2.26518 |

---

### Blocco 10 (Feature 91 - 100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1082 |      11.4262   |
| student_id_S1083 |       0.502885 |
| student_id_S1084 |      -6.20106  |
| student_id_S1085 |       9.3242   |
| student_id_S1086 |      10.8969   |
| student_id_S1087 |     -17.0652   |
| student_id_S1088 |      -3.6771   |
| student_id_S1089 |       6.49862  |
| student_id_S109  |       3.60309  |
| student_id_S1091 |      -3.99051  |

---

### Blocco 11 (Feature 101 - 110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1092 |      -6.4813   |
| student_id_S1093 |      -3.37255  |
| student_id_S1094 |       1.50326  |
| student_id_S1095 |      12.3716   |
| student_id_S1097 |      -0.613754 |
| student_id_S1098 |      10.3125   |
| student_id_S1099 |      -0.126844 |
| student_id_S1101 |      -3.88038  |
| student_id_S1102 |       4.27534  |
| student_id_S1103 |       4.61368  |

---

### Blocco 12 (Feature 111 - 120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1104 |      -5.69819  |
| student_id_S1105 |       3.47873  |
| student_id_S1106 |       0.415127 |
| student_id_S1107 |     -11.0538   |
| student_id_S1108 |      -3.18875  |
| student_id_S1109 |      -5.65592  |
| student_id_S111  |      -7.75152  |
| student_id_S1110 |       0.585485 |
| student_id_S1111 |       4.96383  |
| student_id_S1112 |      13.7865   |

---

### Blocco 13 (Feature 121 - 130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1113 |      5.44805   |
| student_id_S1114 |     -0.414084  |
| student_id_S1116 |      0.0222465 |
| student_id_S1117 |      4.42192   |
| student_id_S1119 |     10.9484    |
| student_id_S112  |      2.9898    |
| student_id_S1120 |     10.3031    |
| student_id_S1121 |      5.82238   |
| student_id_S1122 |      7.31915   |
| student_id_S1123 |      5.55729   |

---

### Blocco 14 (Feature 131 - 140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1124 |      9.35623   |
| student_id_S1125 |     -1.33687   |
| student_id_S1126 |      3.51767   |
| student_id_S1127 |      1.65182   |
| student_id_S1129 |     13.2871    |
| student_id_S1130 |      0.0299425 |
| student_id_S1131 |     -4.04786   |
| student_id_S1132 |     12.4765    |
| student_id_S1133 |     -9.39431   |
| student_id_S1134 |      3.44037   |

---

### Blocco 15 (Feature 141 - 150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1135 |       6.09347  |
| student_id_S1136 |       5.71405  |
| student_id_S1137 |       2.94953  |
| student_id_S1138 |       5.3553   |
| student_id_S1139 |      -5.57143  |
| student_id_S1140 |       0.169406 |
| student_id_S1141 |       2.54208  |
| student_id_S1143 |      11.0906   |
| student_id_S1144 |       3.33129  |
| student_id_S1145 |      -0.246001 |

---

### Blocco 16 (Feature 151 - 160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1146 |      -0.705078 |
| student_id_S1147 |      -3.85158  |
| student_id_S1148 |      -9.85505  |
| student_id_S1149 |       7.01382  |
| student_id_S115  |      -8.06904  |
| student_id_S1150 |      -1.24455  |
| student_id_S1152 |      -3.41666  |
| student_id_S1153 |       9.36754  |
| student_id_S1154 |       5.90357  |
| student_id_S1155 |      -5.86985  |

---

### Blocco 17 (Feature 161 - 170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1156 |       -7.24994 |
| student_id_S1157 |       -1.76259 |
| student_id_S1158 |        2.95366 |
| student_id_S1159 |       -3.00963 |
| student_id_S116  |        3.86873 |
| student_id_S1160 |        6.47288 |
| student_id_S1161 |       -2.00177 |
| student_id_S1162 |       16.9555  |
| student_id_S1163 |        4.17853 |
| student_id_S1165 |      -10.1673  |

---

### Blocco 18 (Feature 171 - 180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1166 |        9.50075 |
| student_id_S1168 |       15.9815  |
| student_id_S1169 |        3.21702 |
| student_id_S117  |       -3.99488 |
| student_id_S1170 |        3.48504 |
| student_id_S1171 |       -3.38904 |
| student_id_S1172 |       -2.53421 |
| student_id_S1174 |        2.21753 |
| student_id_S1175 |        1.20883 |
| student_id_S1176 |       -9.68564 |

---

### Blocco 19 (Feature 181 - 190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1178 |        4.89766 |
| student_id_S118  |        5.47329 |
| student_id_S1180 |        9.87884 |
| student_id_S1181 |        7.9956  |
| student_id_S1183 |       11.2256  |
| student_id_S1184 |        6.50943 |
| student_id_S1185 |        1.65069 |
| student_id_S1186 |        2.41675 |
| student_id_S1187 |      -10.9113  |
| student_id_S1188 |        2.12741 |

---

### Blocco 20 (Feature 191 - 200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1189 |       -1.48215 |
| student_id_S119  |        2.51837 |
| student_id_S1190 |       -1.40637 |
| student_id_S1191 |       12.1974  |
| student_id_S1192 |        2.08966 |
| student_id_S1193 |       15.4848  |
| student_id_S1194 |       -2.13172 |
| student_id_S1195 |       -2.75079 |
| student_id_S1197 |        7.34784 |
| student_id_S1199 |       -2.8414  |

---

### Blocco 21 (Feature 201 - 210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S12   |        9.57456 |
| student_id_S120  |        5.31897 |
| student_id_S1200 |        5.73494 |
| student_id_S1201 |       -2.33838 |
| student_id_S1202 |       10.7904  |
| student_id_S1203 |       12.2699  |
| student_id_S1204 |       -4.16713 |
| student_id_S1205 |      -11.1789  |
| student_id_S1206 |        8.93939 |
| student_id_S1209 |        4.26758 |

---

### Blocco 22 (Feature 211 - 220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1210 |      -1.8012   |
| student_id_S1211 |       9.35529  |
| student_id_S1212 |      -0.202734 |
| student_id_S1213 |      -1.43235  |
| student_id_S1214 |       4.53532  |
| student_id_S1215 |      -3.52097  |
| student_id_S1216 |      -0.343675 |
| student_id_S1218 |       7.52915  |
| student_id_S1219 |       2.6288   |
| student_id_S122  |       2.13115  |

---

### Blocco 23 (Feature 221 - 230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1220 |        7.23267 |
| student_id_S1221 |       -2.55821 |
| student_id_S1222 |       -5.57589 |
| student_id_S1224 |       -3.94225 |
| student_id_S1225 |       -2.54253 |
| student_id_S1226 |       -3.97217 |
| student_id_S1227 |        1.39301 |
| student_id_S1228 |        5.64825 |
| student_id_S1229 |       11.84    |
| student_id_S123  |       -2.33449 |

---

### Blocco 24 (Feature 231 - 240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1230 |      -3.74869  |
| student_id_S1232 |      11.5967   |
| student_id_S1233 |      -6.83648  |
| student_id_S1234 |      -3.57459  |
| student_id_S1235 |      -6.3037   |
| student_id_S1237 |     -11.0494   |
| student_id_S1238 |      -7.22433  |
| student_id_S1239 |       6.62664  |
| student_id_S124  |       3.89363  |
| student_id_S1240 |      -0.410426 |

---

### Blocco 25 (Feature 241 - 250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1241 |       -2.33087 |
| student_id_S1242 |        1.9867  |
| student_id_S1243 |        4.90494 |
| student_id_S1245 |        7.02866 |
| student_id_S1246 |       15.0167  |
| student_id_S1247 |        3.67924 |
| student_id_S1248 |        7.20968 |
| student_id_S1249 |       10.2682  |
| student_id_S125  |       -2.66936 |
| student_id_S1250 |       -9.73336 |

---

### Blocco 26 (Feature 251 - 260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1252 |       8.59911  |
| student_id_S1253 |      -7.44366  |
| student_id_S1254 |       6.57091  |
| student_id_S1255 |      -0.186793 |
| student_id_S1256 |       1.46736  |
| student_id_S1257 |      -7.16865  |
| student_id_S1258 |     -10.4086   |
| student_id_S1259 |      -3.54123  |
| student_id_S1260 |       0.074409 |
| student_id_S1261 |       6.63849  |

---

### Blocco 27 (Feature 261 - 270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1262 |       -7.08008 |
| student_id_S1263 |        1.70122 |
| student_id_S1264 |       10.4168  |
| student_id_S1266 |        5.00632 |
| student_id_S1267 |        1.87454 |
| student_id_S127  |       10.3755  |
| student_id_S1270 |       -6.27307 |
| student_id_S1272 |       -3.00398 |
| student_id_S1273 |        4.40857 |
| student_id_S1274 |       -6.61801 |

---

### Blocco 28 (Feature 271 - 280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1275 |       0.642631 |
| student_id_S1276 |      -3.04379  |
| student_id_S1277 |      -7.90592  |
| student_id_S1278 |       1.28782  |
| student_id_S1279 |      10.4689   |
| student_id_S128  |      -6.14008  |
| student_id_S1280 |       1.04917  |
| student_id_S1281 |       6.36787  |
| student_id_S1282 |       8.73015  |
| student_id_S1283 |       3.24347  |

---

### Blocco 29 (Feature 281 - 290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1284 |       -5.19222 |
| student_id_S1285 |       -6.43086 |
| student_id_S1286 |        7.83284 |
| student_id_S1287 |        9.04428 |
| student_id_S1288 |        3.86381 |
| student_id_S129  |        2.36254 |
| student_id_S1290 |        6.7829  |
| student_id_S1291 |        5.31042 |
| student_id_S1292 |        5.72887 |
| student_id_S1293 |        1.39133 |

---

### Blocco 30 (Feature 291 - 300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1294 |        6.78889 |
| student_id_S1295 |        9.72249 |
| student_id_S1296 |       -3.87821 |
| student_id_S1297 |        1.58894 |
| student_id_S1298 |        6.34804 |
| student_id_S1299 |       -5.33994 |
| student_id_S13   |       10.5585  |
| student_id_S130  |       -4.61877 |
| student_id_S1300 |        5.56906 |
| student_id_S1301 |        2.07047 |

---

### Blocco 31 (Feature 301 - 310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1302 |       6.24088  |
| student_id_S1304 |       1.25913  |
| student_id_S1305 |      10.9166   |
| student_id_S1306 |      -1.24454  |
| student_id_S1307 |     -11.4935   |
| student_id_S1309 |       1.46408  |
| student_id_S131  |       3.92039  |
| student_id_S1310 |       0.688499 |
| student_id_S1311 |       2.39159  |
| student_id_S1312 |      -3.6932   |

---

### Blocco 32 (Feature 311 - 320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1313 |        3.73138 |
| student_id_S1314 |        5.27612 |
| student_id_S1315 |        6.22752 |
| student_id_S1317 |        6.32772 |
| student_id_S1318 |        3.90607 |
| student_id_S132  |       -1.94459 |
| student_id_S1320 |        1.27387 |
| student_id_S1322 |       -6.4924  |
| student_id_S1323 |       -4.0261  |
| student_id_S1325 |        5.29518 |

---

### Blocco 33 (Feature 321 - 330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1326 |      -9.81553  |
| student_id_S1327 |       7.28808  |
| student_id_S1329 |       1.97385  |
| student_id_S133  |      -6.0161   |
| student_id_S1330 |      14.344    |
| student_id_S1331 |       0.100173 |
| student_id_S1332 |      10.4417   |
| student_id_S1333 |      -1.75121  |
| student_id_S1334 |     -16.8297   |
| student_id_S1335 |       2.4827   |

---

### Blocco 34 (Feature 331 - 340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1336 |       -8.86584 |
| student_id_S1338 |        5.10947 |
| student_id_S1339 |        9.67557 |
| student_id_S134  |       -6.38314 |
| student_id_S1341 |        8.75904 |
| student_id_S1342 |        6.36326 |
| student_id_S1343 |       -2.86964 |
| student_id_S1344 |        5.20426 |
| student_id_S1345 |        9.79725 |
| student_id_S1349 |       -6.6646  |

---

### Blocco 35 (Feature 341 - 350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S135  |      10.0545   |
| student_id_S1350 |       8.3917   |
| student_id_S1351 |       9.64029  |
| student_id_S1352 |      -2.81989  |
| student_id_S1353 |      -3.24395  |
| student_id_S1354 |       7.84011  |
| student_id_S1355 |       0.221032 |
| student_id_S1356 |       1.7831   |
| student_id_S1357 |       3.75748  |
| student_id_S1358 |      -9.72681  |

---

### Blocco 36 (Feature 351 - 360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1359 |       -4.12848 |
| student_id_S136  |       11.2094  |
| student_id_S1360 |       -5.46292 |
| student_id_S1361 |       -7.07162 |
| student_id_S1362 |        1.58157 |
| student_id_S1363 |        9.42785 |
| student_id_S1364 |       -1.26163 |
| student_id_S1365 |       -0.90339 |
| student_id_S1366 |        3.5891  |
| student_id_S1367 |       14.343   |

---

### Blocco 37 (Feature 361 - 370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1368 |       -1.88785 |
| student_id_S1369 |        1.6884  |
| student_id_S137  |        4.57483 |
| student_id_S1370 |       -8.91925 |
| student_id_S1371 |        1.01405 |
| student_id_S1372 |       -2.38765 |
| student_id_S1373 |       -8.17594 |
| student_id_S1374 |       12.6975  |
| student_id_S1375 |       11.9618  |
| student_id_S1377 |       -6.26985 |

---

### Blocco 38 (Feature 371 - 380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1378 |       0.712946 |
| student_id_S1379 |      -0.120536 |
| student_id_S1380 |       7.0848   |
| student_id_S1381 |      -3.70312  |
| student_id_S1382 |       1.40633  |
| student_id_S1383 |       0.197305 |
| student_id_S1384 |       0.113655 |
| student_id_S1385 |      -3.07728  |
| student_id_S1386 |      10.1002   |
| student_id_S1387 |      -5.7011   |

---

### Blocco 39 (Feature 381 - 390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1388 |      3.91764   |
| student_id_S1389 |      3.12178   |
| student_id_S139  |     -7.99339   |
| student_id_S1391 |    -11.1087    |
| student_id_S1392 |     -5.56023   |
| student_id_S1393 |      0.0185289 |
| student_id_S1394 |      7.49727   |
| student_id_S1395 |     -0.217923  |
| student_id_S1396 |     -3.96908   |
| student_id_S1397 |     -1.59534   |

---

### Blocco 40 (Feature 391 - 400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1398 |       -6.63229 |
| student_id_S1399 |       -1.44958 |
| student_id_S1400 |        1.78251 |
| student_id_S1401 |        2.57218 |
| student_id_S1402 |        6.61333 |
| student_id_S1403 |       -6.55644 |
| student_id_S1404 |       -0.39764 |
| student_id_S1405 |        2.73007 |
| student_id_S1407 |       -8.49422 |
| student_id_S1409 |        3.68961 |

---

### Blocco 41 (Feature 401 - 410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S141  |       -1.07711 |
| student_id_S1410 |       -9.43266 |
| student_id_S1411 |        5.89471 |
| student_id_S1413 |       -5.92316 |
| student_id_S1414 |       -7.31599 |
| student_id_S1415 |       -9.22635 |
| student_id_S1416 |      -11.376   |
| student_id_S1417 |       13.4079  |
| student_id_S1419 |        1.44607 |
| student_id_S142  |      -12.563   |

---

### Blocco 42 (Feature 411 - 420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1421 |        7.13614 |
| student_id_S1422 |       -7.79492 |
| student_id_S1423 |        1.30602 |
| student_id_S1424 |       10.3058  |
| student_id_S1425 |        2.94148 |
| student_id_S1426 |        7.28753 |
| student_id_S1427 |        4.32561 |
| student_id_S1428 |        1.4144  |
| student_id_S1429 |      -11.4458  |
| student_id_S143  |       -5.52023 |

---

### Blocco 43 (Feature 421 - 430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1430 |       12.2919  |
| student_id_S1431 |        2.80606 |
| student_id_S1432 |       -4.06795 |
| student_id_S1433 |        7.99984 |
| student_id_S1434 |       -6.59602 |
| student_id_S1435 |        1.10576 |
| student_id_S1437 |        8.4681  |
| student_id_S1438 |       -2.5523  |
| student_id_S1439 |       -4.28669 |
| student_id_S144  |        1.10613 |

---

### Blocco 44 (Feature 431 - 440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1440 |        2.3576  |
| student_id_S1441 |       13.9871  |
| student_id_S1442 |       -4.20803 |
| student_id_S1443 |      -10.5129  |
| student_id_S1444 |        5.66817 |
| student_id_S1445 |       -5.38501 |
| student_id_S1446 |       -9.59636 |
| student_id_S1447 |      -11.1979  |
| student_id_S1448 |       -7.26175 |
| student_id_S1449 |        7.77798 |

---

### Blocco 45 (Feature 441 - 450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S145  |      0.0663529 |
| student_id_S1450 |      3.77318   |
| student_id_S1452 |     -3.35517   |
| student_id_S1453 |      1.21161   |
| student_id_S1456 |     -2.77223   |
| student_id_S1457 |    -11.3737    |
| student_id_S1458 |      2.77871   |
| student_id_S1459 |      9.80456   |
| student_id_S146  |     -3.98935   |
| student_id_S1460 |     18.4444    |

---

### Blocco 46 (Feature 451 - 460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1461 |      -4.02424  |
| student_id_S1462 |      -8.62067  |
| student_id_S1463 |       5.25534  |
| student_id_S1464 |       0.348139 |
| student_id_S1465 |      -9.72824  |
| student_id_S1466 |      -1.43276  |
| student_id_S1467 |       1.18583  |
| student_id_S1468 |     -10.9771   |
| student_id_S1469 |       3.40212  |
| student_id_S147  |      15.3405   |

---

### Blocco 47 (Feature 461 - 470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1470 |       7.03266  |
| student_id_S1471 |      -2.88835  |
| student_id_S1473 |       0.522253 |
| student_id_S1474 |       3.46079  |
| student_id_S1475 |       4.20224  |
| student_id_S1476 |       8.43766  |
| student_id_S1477 |       9.58576  |
| student_id_S1478 |      -0.761971 |
| student_id_S1479 |      10.5197   |
| student_id_S148  |       0.890602 |

---

### Blocco 48 (Feature 471 - 480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1481 |        6.42643 |
| student_id_S1482 |       -1.14351 |
| student_id_S1483 |        7.2457  |
| student_id_S1484 |        7.92072 |
| student_id_S1485 |        4.05554 |
| student_id_S1486 |        9.94776 |
| student_id_S1487 |        8.56673 |
| student_id_S1488 |       -9.61128 |
| student_id_S1489 |       -1.74215 |
| student_id_S149  |       -3.02191 |

---

### Blocco 49 (Feature 481 - 490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1490 |       13.8731  |
| student_id_S1491 |        3.96767 |
| student_id_S1492 |        5.25961 |
| student_id_S1494 |        5.78681 |
| student_id_S1495 |      -10.0157  |
| student_id_S1496 |        9.10033 |
| student_id_S1497 |        2.51815 |
| student_id_S1498 |       -8.29761 |
| student_id_S1499 |        5.78392 |
| student_id_S15   |       -1.47447 |

---

### Blocco 50 (Feature 491 - 500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S150  |       8.08664  |
| student_id_S1500 |      -5.78377  |
| student_id_S1501 |       4.9572   |
| student_id_S1502 |       2.74664  |
| student_id_S1503 |       1.40973  |
| student_id_S1504 |     -17.3529   |
| student_id_S1505 |      -2.5216   |
| student_id_S1506 |       0.291782 |
| student_id_S1508 |      10.1529   |
| student_id_S151  |       1.02976  |

---

### Blocco 51 (Feature 501 - 510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1510 |       0.740757 |
| student_id_S1511 |       4.53941  |
| student_id_S1512 |      -7.45194  |
| student_id_S1513 |      15.4072   |
| student_id_S1514 |      -0.474347 |
| student_id_S1516 |      -2.3278   |
| student_id_S1517 |     -16.907    |
| student_id_S1518 |       3.83351  |
| student_id_S1519 |      11.322    |
| student_id_S152  |      -7.03875  |

---

### Blocco 52 (Feature 511 - 520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1520 |        7.72808 |
| student_id_S1521 |       -4.42764 |
| student_id_S1522 |        2.80091 |
| student_id_S1523 |      -13.7528  |
| student_id_S1524 |        2.22211 |
| student_id_S1525 |        5.92185 |
| student_id_S1526 |      -12.4581  |
| student_id_S1527 |       10.2325  |
| student_id_S1529 |       10.4627  |
| student_id_S153  |       11.4169  |

---

### Blocco 53 (Feature 521 - 530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1530 |      -4.97602  |
| student_id_S1531 |      14.2666   |
| student_id_S1532 |       0.978754 |
| student_id_S1533 |       5.27078  |
| student_id_S1534 |      -6.50383  |
| student_id_S1535 |       3.55587  |
| student_id_S1536 |       3.79038  |
| student_id_S1537 |       2.66844  |
| student_id_S1538 |       9.20589  |
| student_id_S154  |       3.33412  |

---

### Blocco 54 (Feature 531 - 540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1540 |        7.60426 |
| student_id_S1541 |      -12.7097  |
| student_id_S1542 |        1.87869 |
| student_id_S1543 |       -7.29228 |
| student_id_S1544 |        2.37222 |
| student_id_S1545 |        1.23478 |
| student_id_S1546 |        6.50416 |
| student_id_S1547 |      -10.2668  |
| student_id_S1548 |        1.17858 |
| student_id_S1549 |       17.8324  |

---

### Blocco 55 (Feature 541 - 550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S155  |     -10.0838   |
| student_id_S1550 |       4.43248  |
| student_id_S1551 |      -8.30195  |
| student_id_S1552 |       5.71673  |
| student_id_S1553 |      13.3472   |
| student_id_S1554 |      -0.649035 |
| student_id_S1555 |      -1.68925  |
| student_id_S1556 |      -5.89791  |
| student_id_S1558 |      11.5531   |
| student_id_S1559 |      -1.51462  |

---

### Blocco 56 (Feature 551 - 560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S156  |       0.15708  |
| student_id_S1560 |      -1.60132  |
| student_id_S1561 |       4.77698  |
| student_id_S1562 |       4.81792  |
| student_id_S1563 |      -3.38397  |
| student_id_S1564 |       0.260666 |
| student_id_S1566 |       5.68731  |
| student_id_S1568 |     -10.1682   |
| student_id_S1569 |       3.19279  |
| student_id_S157  |     -12.7186   |

---

### Blocco 57 (Feature 561 - 570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1570 |        7.35117 |
| student_id_S1571 |       -3.10468 |
| student_id_S1572 |       -4.97838 |
| student_id_S1573 |        4.47874 |
| student_id_S1574 |       -3.66619 |
| student_id_S1575 |        8.6933  |
| student_id_S1576 |        7.33778 |
| student_id_S1577 |       -5.98339 |
| student_id_S1578 |       -7.52992 |
| student_id_S158  |        5.90974 |

---

### Blocco 58 (Feature 571 - 580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1580 |       6.68661  |
| student_id_S1581 |      -3.83757  |
| student_id_S1582 |      -5.012    |
| student_id_S1583 |       0.821606 |
| student_id_S1584 |       1.8023   |
| student_id_S1585 |      -2.90595  |
| student_id_S1587 |       3.00174  |
| student_id_S1588 |       0.231079 |
| student_id_S1589 |      -7.20147  |
| student_id_S159  |      -0.827703 |

---

### Blocco 59 (Feature 581 - 590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1590 |       11.4093  |
| student_id_S1591 |       -3.49665 |
| student_id_S1592 |       10.7717  |
| student_id_S1593 |       -2.83114 |
| student_id_S1595 |       -4.64522 |
| student_id_S1596 |        6.7487  |
| student_id_S1597 |       -1.60564 |
| student_id_S1598 |      -13.6465  |
| student_id_S1599 |       -1.71367 |
| student_id_S16   |       -4.66191 |

---

### Blocco 60 (Feature 591 - 600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1600 |        4.60092 |
| student_id_S1603 |       -7.18028 |
| student_id_S1605 |       -3.16671 |
| student_id_S1606 |       10.3406  |
| student_id_S1607 |        3.08401 |
| student_id_S1608 |       -5.84721 |
| student_id_S1609 |        0.90812 |
| student_id_S1611 |        8.10157 |
| student_id_S1612 |        2.11805 |
| student_id_S1613 |       15.1756  |

---

### Blocco 61 (Feature 601 - 610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1614 |      -2.65688  |
| student_id_S1615 |       0.345499 |
| student_id_S1616 |       0.885186 |
| student_id_S1617 |       4.52607  |
| student_id_S1618 |      -9.508    |
| student_id_S1619 |       1.94052  |
| student_id_S162  |       3.40459  |
| student_id_S1620 |       6.25829  |
| student_id_S1621 |      -6.10323  |
| student_id_S1622 |     -14.4672   |

---

### Blocco 62 (Feature 611 - 620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1623 |       4.03599  |
| student_id_S1625 |       1.95807  |
| student_id_S1626 |      -4.37178  |
| student_id_S1627 |     -13.2754   |
| student_id_S1629 |      -0.967632 |
| student_id_S163  |      -1.45037  |
| student_id_S1630 |       6.35772  |
| student_id_S1631 |     -12.3589   |
| student_id_S1632 |      -1.11898  |
| student_id_S1634 |      10.1011   |

---

### Blocco 63 (Feature 621 - 630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1635 |        2.44263 |
| student_id_S1636 |       -3.96906 |
| student_id_S1637 |       15.3807  |
| student_id_S1638 |       -5.19046 |
| student_id_S1639 |        8.81768 |
| student_id_S164  |        1.0364  |
| student_id_S1640 |        3.99858 |
| student_id_S1641 |        7.39881 |
| student_id_S1643 |       -2.89025 |
| student_id_S1644 |        2.21234 |

---

### Blocco 64 (Feature 631 - 640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1645 |       6.428    |
| student_id_S1646 |       8.22255  |
| student_id_S1648 |     -11.1236   |
| student_id_S1649 |      -2.10758  |
| student_id_S165  |      -1.12381  |
| student_id_S1650 |      -8.80939  |
| student_id_S1651 |      -3.27922  |
| student_id_S1652 |       0.554394 |
| student_id_S1653 |      13.7384   |
| student_id_S1655 |       0.399191 |

---

### Blocco 65 (Feature 641 - 650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1656 |       7.16969  |
| student_id_S1657 |       4.14713  |
| student_id_S1658 |       3.93445  |
| student_id_S1659 |      -2.22008  |
| student_id_S166  |      -1.91689  |
| student_id_S1660 |      -4.86586  |
| student_id_S1661 |       0.800699 |
| student_id_S1662 |      -4.41474  |
| student_id_S1663 |      -0.949451 |
| student_id_S1664 |      -8.95722  |

---

### Blocco 66 (Feature 651 - 660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1665 |       10.0374  |
| student_id_S1667 |        3.74811 |
| student_id_S1668 |        8.65703 |
| student_id_S1669 |      -12.973   |
| student_id_S167  |        3.17046 |
| student_id_S1670 |       -5.26771 |
| student_id_S1671 |       -7.4276  |
| student_id_S1673 |       -2.7543  |
| student_id_S1674 |       12.7127  |
| student_id_S1675 |        8.21907 |

---

### Blocco 67 (Feature 661 - 670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1677 |       -5.34609 |
| student_id_S1678 |        4.66004 |
| student_id_S1679 |       -7.19738 |
| student_id_S1680 |        5.28573 |
| student_id_S1681 |       -8.41832 |
| student_id_S1682 |      -10.022   |
| student_id_S1683 |       -6.39948 |
| student_id_S1684 |       12.411   |
| student_id_S1686 |       -5.10385 |
| student_id_S1687 |        7.95335 |

---

### Blocco 68 (Feature 671 - 680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1689 |       4.10036  |
| student_id_S1690 |       0.241857 |
| student_id_S1691 |       8.89638  |
| student_id_S1692 |       1.64379  |
| student_id_S1693 |       1.83909  |
| student_id_S1694 |       8.03718  |
| student_id_S1695 |       5.58623  |
| student_id_S1696 |     -11.2865   |
| student_id_S1697 |      -6.34691  |
| student_id_S1698 |      -5.60118  |

---

### Blocco 69 (Feature 681 - 690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1699 |        1.15961 |
| student_id_S17   |       -4.50611 |
| student_id_S170  |       -1.99521 |
| student_id_S1701 |        1.7182  |
| student_id_S1702 |        9.76366 |
| student_id_S1703 |       -5.80286 |
| student_id_S1704 |        8.92201 |
| student_id_S1705 |        8.24451 |
| student_id_S1706 |       -9.79644 |
| student_id_S1707 |        1.53332 |

---

### Blocco 70 (Feature 691 - 700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1708 |       0.156858 |
| student_id_S1709 |      -2.38223  |
| student_id_S171  |       0.599376 |
| student_id_S1711 |      -5.49089  |
| student_id_S1713 |      -7.41687  |
| student_id_S1715 |      -1.28525  |
| student_id_S1716 |      -5.19057  |
| student_id_S1717 |      10.1166   |
| student_id_S1718 |       6.36294  |
| student_id_S1719 |      -6.27064  |

---

### Blocco 71 (Feature 701 - 710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S172  |     11.8899    |
| student_id_S1720 |     -3.37879   |
| student_id_S1721 |     -7.14195   |
| student_id_S1722 |      5.52676   |
| student_id_S1723 |      9.17821   |
| student_id_S1724 |      0.0296612 |
| student_id_S1725 |     -3.12456   |
| student_id_S1726 |    -10.4231    |
| student_id_S1727 |     -9.01871   |
| student_id_S1728 |     -4.5512    |

---

### Blocco 72 (Feature 711 - 720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1729 |      -0.235864 |
| student_id_S173  |      -0.517685 |
| student_id_S1730 |     -10.263    |
| student_id_S1732 |     -13.2045   |
| student_id_S1733 |       1.73911  |
| student_id_S1734 |      -4.98389  |
| student_id_S1735 |      11.8512   |
| student_id_S1736 |      -0.788557 |
| student_id_S1737 |       0.86148  |
| student_id_S1738 |     -10.3448   |

---

### Blocco 73 (Feature 721 - 730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S174  |       -6.57629 |
| student_id_S1740 |        3.94691 |
| student_id_S1741 |       -4.2245  |
| student_id_S1745 |       11.2529  |
| student_id_S1746 |        3.31005 |
| student_id_S1747 |       -1.87358 |
| student_id_S1748 |       -7.31952 |
| student_id_S1749 |       -1.65132 |
| student_id_S175  |       -1.84231 |
| student_id_S1750 |        7.80832 |

---

### Blocco 74 (Feature 731 - 740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1751 |       4.42142  |
| student_id_S1753 |      -0.644223 |
| student_id_S1754 |      -5.25857  |
| student_id_S1757 |      -3.86061  |
| student_id_S1758 |      -8.14146  |
| student_id_S1759 |       2.05965  |
| student_id_S176  |       9.30036  |
| student_id_S1760 |      14.8331   |
| student_id_S1761 |      -0.800361 |
| student_id_S1762 |       3.26644  |

---

### Blocco 75 (Feature 741 - 750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1763 |       5.53687  |
| student_id_S1765 |       0.907948 |
| student_id_S1766 |      -7.39855  |
| student_id_S1767 |       6.6599   |
| student_id_S1768 |     -15.2015   |
| student_id_S1769 |      11.7137   |
| student_id_S177  |      -7.2606   |
| student_id_S1770 |      10.397    |
| student_id_S1771 |       4.16407  |
| student_id_S1772 |       0.753598 |

---

### Blocco 76 (Feature 751 - 760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1773 |        9.69073 |
| student_id_S1774 |        3.77421 |
| student_id_S1775 |        2.6162  |
| student_id_S1776 |        4.67289 |
| student_id_S1777 |       -7.01211 |
| student_id_S1778 |        2.82722 |
| student_id_S1779 |      -12.2522  |
| student_id_S178  |       -8.56118 |
| student_id_S1780 |        6.85259 |
| student_id_S1781 |       10.4022  |

---

### Blocco 77 (Feature 761 - 770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1782 |       0.500772 |
| student_id_S1783 |       3.29777  |
| student_id_S1784 |      13.3127   |
| student_id_S1785 |      -1.62693  |
| student_id_S1787 |      -7.67575  |
| student_id_S1788 |       9.27643  |
| student_id_S1789 |      -6.21923  |
| student_id_S179  |       5.10813  |
| student_id_S1790 |      -9.31764  |
| student_id_S1791 |     -11.6985   |

---

### Blocco 78 (Feature 771 - 780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1792 |        6.00212 |
| student_id_S1793 |        3.99714 |
| student_id_S1794 |       -4.36522 |
| student_id_S1795 |       -1.5437  |
| student_id_S1798 |       -8.30218 |
| student_id_S1799 |       -3.23231 |
| student_id_S180  |       -2.13093 |
| student_id_S1800 |       -1.99476 |
| student_id_S1801 |      -10.2057  |
| student_id_S1802 |        2.09268 |

---

### Blocco 79 (Feature 781 - 790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1803 |       -9.9418  |
| student_id_S1804 |      -12.5674  |
| student_id_S1805 |        4.78508 |
| student_id_S1806 |        1.58719 |
| student_id_S1807 |       -6.51664 |
| student_id_S1808 |       -8.68746 |
| student_id_S1809 |        3.39391 |
| student_id_S181  |        1.24044 |
| student_id_S1811 |        8.39547 |
| student_id_S1813 |        4.59469 |

---

### Blocco 80 (Feature 791 - 800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1815 |       8.7229   |
| student_id_S1816 |       3.7556   |
| student_id_S1818 |       8.32814  |
| student_id_S1819 |      -0.206923 |
| student_id_S182  |      -0.196484 |
| student_id_S1820 |       2.41604  |
| student_id_S1821 |      -4.36927  |
| student_id_S1822 |      -5.81262  |
| student_id_S1825 |       4.62926  |
| student_id_S1826 |       4.63971  |

---

### Blocco 81 (Feature 801 - 810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1827 |       5.32461  |
| student_id_S1828 |       2.50193  |
| student_id_S1829 |      11.4186   |
| student_id_S183  |       5.45219  |
| student_id_S1830 |      -3.91085  |
| student_id_S1831 |       8.1017   |
| student_id_S1832 |       5.93352  |
| student_id_S1833 |       0.411966 |
| student_id_S1834 |      -6.01792  |
| student_id_S1835 |      -1.45223  |

---

### Blocco 82 (Feature 811 - 820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1836 |       2.66876  |
| student_id_S1837 |       6.54788  |
| student_id_S1838 |      -1.12388  |
| student_id_S1839 |      -4.11954  |
| student_id_S184  |     -10.1318   |
| student_id_S1840 |      -7.51465  |
| student_id_S1841 |     -14.2628   |
| student_id_S1842 |      -1.2652   |
| student_id_S1844 |      -0.605449 |
| student_id_S1845 |      -1.97742  |

---

### Blocco 83 (Feature 821 - 830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1848 |     2.76122    |
| student_id_S185  |     2.64569    |
| student_id_S1850 |    -0.174013   |
| student_id_S1853 |    -1.7058     |
| student_id_S1855 |     1.29571    |
| student_id_S1856 |    -0.577666   |
| student_id_S1857 |     7.57252    |
| student_id_S1858 |     6.04049    |
| student_id_S1859 |     0.00355698 |
| student_id_S186  |    17.0223     |

---

### Blocco 84 (Feature 831 - 840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1860 |       -3.24522 |
| student_id_S1861 |       -2.99347 |
| student_id_S1863 |       -5.39575 |
| student_id_S1864 |       -9.47277 |
| student_id_S1865 |        9.5087  |
| student_id_S1866 |       -1.01208 |
| student_id_S1867 |        7.78493 |
| student_id_S1868 |        1.25472 |
| student_id_S1869 |        4.56377 |
| student_id_S187  |       -2.48706 |

---

### Blocco 85 (Feature 841 - 850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1870 |        4.98568 |
| student_id_S1872 |        1.91978 |
| student_id_S1873 |       -7.71711 |
| student_id_S1875 |       -2.02366 |
| student_id_S1876 |       -6.01638 |
| student_id_S1877 |       17.529   |
| student_id_S1878 |       -8.33642 |
| student_id_S1879 |       -8.11694 |
| student_id_S188  |       -6.22992 |
| student_id_S1880 |        8.07349 |

---

### Blocco 86 (Feature 851 - 860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1883 |      2.82438   |
| student_id_S1884 |     -5.65001   |
| student_id_S1885 |     -5.6613    |
| student_id_S1886 |     -8.75621   |
| student_id_S1887 |     -5.03107   |
| student_id_S1888 |     -0.0365553 |
| student_id_S189  |     -0.384828  |
| student_id_S1890 |      6.00207   |
| student_id_S1891 |      0.371472  |
| student_id_S1892 |     -4.36928   |

---

### Blocco 87 (Feature 861 - 870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1893 |        0.79375 |
| student_id_S1894 |        7.62026 |
| student_id_S1895 |        1.87447 |
| student_id_S1896 |       -5.83686 |
| student_id_S1897 |        6.26497 |
| student_id_S1898 |      -13.6093  |
| student_id_S1899 |       -7.93067 |
| student_id_S190  |       -4.484   |
| student_id_S1900 |       -8.08004 |
| student_id_S1901 |       -6.10278 |

---

### Blocco 88 (Feature 871 - 880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1902 |      -3.40603  |
| student_id_S1903 |       0.832767 |
| student_id_S1904 |       0.523818 |
| student_id_S1905 |      14.7635   |
| student_id_S1906 |       1.76869  |
| student_id_S1907 |       9.50703  |
| student_id_S1908 |     -14.2865   |
| student_id_S1909 |      -3.66523  |
| student_id_S1910 |     -11.3886   |
| student_id_S1911 |       4.62838  |

---

### Blocco 89 (Feature 881 - 890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1912 |     -16.1034   |
| student_id_S1913 |       2.03423  |
| student_id_S1914 |      -4.44235  |
| student_id_S1915 |       9.35379  |
| student_id_S1917 |      -7.2595   |
| student_id_S1918 |      -2.96208  |
| student_id_S1919 |      -0.65452  |
| student_id_S192  |      -7.46807  |
| student_id_S1920 |      -0.910874 |
| student_id_S1922 |       1.58294  |

---

### Blocco 90 (Feature 891 - 900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1923 |      -5.73402  |
| student_id_S1924 |      -0.755815 |
| student_id_S1925 |       1.32558  |
| student_id_S1926 |      11.1764   |
| student_id_S1927 |       7.45224  |
| student_id_S1928 |       9.37143  |
| student_id_S1929 |       2.83648  |
| student_id_S193  |       3.74133  |
| student_id_S1930 |      -0.542688 |
| student_id_S1931 |       5.82416  |

---

### Blocco 91 (Feature 901 - 910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1932 |      -13.8566  |
| student_id_S1934 |       -9.34862 |
| student_id_S1935 |       -6.20143 |
| student_id_S1936 |       -6.28535 |
| student_id_S1937 |       -7.95686 |
| student_id_S1938 |        4.23634 |
| student_id_S1939 |        3.6089  |
| student_id_S194  |       -1.26811 |
| student_id_S1940 |       -4.08934 |
| student_id_S1941 |      -11.4643  |

---

### Blocco 92 (Feature 911 - 920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1942 |     -1.11106   |
| student_id_S1943 |     12.1199    |
| student_id_S1944 |      7.56196   |
| student_id_S1946 |      0.0864889 |
| student_id_S1947 |      6.5442    |
| student_id_S1948 |     -6.42209   |
| student_id_S1949 |      2.8145    |
| student_id_S195  |     -9.8234    |
| student_id_S1950 |     -5.42681   |
| student_id_S1951 |     15.037     |

---

### Blocco 93 (Feature 921 - 930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1952 |       8.74615  |
| student_id_S1953 |       2.5499   |
| student_id_S1954 |       5.43812  |
| student_id_S1955 |       3.58949  |
| student_id_S1956 |      14.1349   |
| student_id_S1957 |       7.28552  |
| student_id_S1958 |      -7.03052  |
| student_id_S1959 |       1.55168  |
| student_id_S196  |      -0.301776 |
| student_id_S1960 |      18.9025   |

---

### Blocco 94 (Feature 931 - 940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1961 |       3.31731  |
| student_id_S1962 |       0.216636 |
| student_id_S1963 |      -2.34336  |
| student_id_S1964 |      -7.78864  |
| student_id_S1965 |       0.501843 |
| student_id_S1966 |      -4.7676   |
| student_id_S1968 |       0.771826 |
| student_id_S1969 |      -5.79043  |
| student_id_S197  |       6.59196  |
| student_id_S1971 |      -8.3013   |

---

### Blocco 95 (Feature 941 - 950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1972 |       3.28211  |
| student_id_S1973 |      -5.79492  |
| student_id_S1974 |       6.46175  |
| student_id_S1975 |      13.506    |
| student_id_S1976 |      -7.17111  |
| student_id_S1977 |      -0.191993 |
| student_id_S1978 |      -0.821093 |
| student_id_S1979 |       7.68644  |
| student_id_S198  |      -4.67928  |
| student_id_S1980 |      -8.73665  |

---

### Blocco 96 (Feature 951 - 960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1981 |       -6.12898 |
| student_id_S1982 |       -3.22795 |
| student_id_S1983 |       -3.62291 |
| student_id_S1984 |        6.11737 |
| student_id_S1985 |        1.78381 |
| student_id_S1987 |       12.1907  |
| student_id_S199  |        1.15905 |
| student_id_S1990 |      -13.7832  |
| student_id_S1993 |        6.61936 |
| student_id_S1994 |        9.90971 |

---

### Blocco 97 (Feature 961 - 970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S1995 |       0.747416 |
| student_id_S1996 |      -7.82738  |
| student_id_S1997 |       2.59561  |
| student_id_S1998 |      -7.52998  |
| student_id_S1999 |       2.03907  |
| student_id_S2    |       7.06951  |
| student_id_S20   |      13.5452   |
| student_id_S200  |     -12.7113   |
| student_id_S2000 |      16.4841   |
| student_id_S2001 |       4.20764  |

---

### Blocco 98 (Feature 971 - 980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2002 |       1.43277  |
| student_id_S2003 |       3.62972  |
| student_id_S2004 |       8.97384  |
| student_id_S2005 |      -6.48925  |
| student_id_S2006 |      -4.11723  |
| student_id_S2007 |      -9.61091  |
| student_id_S2009 |       0.656641 |
| student_id_S201  |      -4.34952  |
| student_id_S2010 |       6.06126  |
| student_id_S2011 |      -5.30741  |

---

### Blocco 99 (Feature 981 - 990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2012 |      -0.593062 |
| student_id_S2013 |       2.68377  |
| student_id_S2014 |       1.35592  |
| student_id_S2015 |      -5.85473  |
| student_id_S2016 |      -4.31667  |
| student_id_S2017 |       0.620175 |
| student_id_S2019 |       0.273532 |
| student_id_S2020 |      -0.23215  |
| student_id_S2021 |      -6.54433  |
| student_id_S2022 |       2.74517  |

---

### Blocco 100 (Feature 991 - 1000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2023 |        1.5832  |
| student_id_S2024 |       -3.55838 |
| student_id_S2026 |      -13.8192  |
| student_id_S2027 |        7.2309  |
| student_id_S2028 |        9.67253 |
| student_id_S2029 |      -12.9496  |
| student_id_S203  |        3.00219 |
| student_id_S2030 |       -5.15414 |
| student_id_S2033 |       -8.00256 |
| student_id_S2034 |        4.30799 |

---

### Blocco 101 (Feature 1001 - 1010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2035 |      -0.315546 |
| student_id_S2036 |       0.861424 |
| student_id_S2037 |       7.30492  |
| student_id_S2038 |     -12.2373   |
| student_id_S2039 |      -9.61131  |
| student_id_S204  |      -5.34617  |
| student_id_S2040 |     -15.3883   |
| student_id_S2041 |       0.187907 |
| student_id_S2043 |      12.912    |
| student_id_S2045 |       7.15998  |

---

### Blocco 102 (Feature 1011 - 1020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2047 |     -5.82058   |
| student_id_S2048 |     -0.0369166 |
| student_id_S2049 |     -1.20124   |
| student_id_S205  |      9.11245   |
| student_id_S2050 |     10.7902    |
| student_id_S2051 |     -6.47588   |
| student_id_S2052 |     -4.13472   |
| student_id_S2053 |     -5.90041   |
| student_id_S2054 |     -5.05575   |
| student_id_S2055 |      2.75176   |

---

### Blocco 103 (Feature 1021 - 1030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2056 |       4.87139  |
| student_id_S2057 |       5.2647   |
| student_id_S2058 |       0.565611 |
| student_id_S2059 |      -1.11359  |
| student_id_S206  |      -3.76345  |
| student_id_S2060 |       3.69129  |
| student_id_S2061 |     -12.361    |
| student_id_S2062 |       2.20852  |
| student_id_S2063 |      11.8354   |
| student_id_S2064 |       2.30869  |

---

### Blocco 104 (Feature 1031 - 1040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2065 |     -13.5277   |
| student_id_S2067 |       1.78488  |
| student_id_S2068 |      -4.3564   |
| student_id_S207  |       0.867581 |
| student_id_S2070 |      -0.229207 |
| student_id_S2071 |       0.795413 |
| student_id_S2073 |       1.99336  |
| student_id_S2074 |       9.11308  |
| student_id_S2075 |      10.6977   |
| student_id_S2076 |       4.62611  |

---

### Blocco 105 (Feature 1041 - 1050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2077 |      5.78729   |
| student_id_S2079 |     -2.98993   |
| student_id_S208  |      4.3103    |
| student_id_S2081 |     -3.84857   |
| student_id_S2082 |      7.484     |
| student_id_S2083 |      0.0941972 |
| student_id_S2085 |     -2.27795   |
| student_id_S2086 |     -3.41414   |
| student_id_S2087 |     -6.59454   |
| student_id_S2089 |      7.31484   |

---

### Blocco 106 (Feature 1051 - 1060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S209  |       -4.55655 |
| student_id_S2091 |       -7.60421 |
| student_id_S2092 |       -3.11062 |
| student_id_S2093 |      -13.4848  |
| student_id_S2094 |       12.5936  |
| student_id_S2095 |       12.6676  |
| student_id_S2096 |       -0.11105 |
| student_id_S2098 |        5.7232  |
| student_id_S2099 |       -3.60141 |
| student_id_S21   |        9.7844  |

---

### Blocco 107 (Feature 1061 - 1070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S210  |      -3.4553   |
| student_id_S2100 |      -0.587864 |
| student_id_S2102 |       0.168516 |
| student_id_S2103 |      -5.93269  |
| student_id_S2104 |      11.5666   |
| student_id_S2105 |      -1.57138  |
| student_id_S2106 |     -11.007    |
| student_id_S2107 |       3.05863  |
| student_id_S2108 |      -2.87912  |
| student_id_S2109 |       4.68918  |

---

### Blocco 108 (Feature 1071 - 1080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S211  |        1.5182  |
| student_id_S2110 |       -6.71722 |
| student_id_S2111 |        2.08576 |
| student_id_S2112 |        4.59958 |
| student_id_S2114 |        4.66698 |
| student_id_S2116 |        1.0988  |
| student_id_S2117 |       -4.60014 |
| student_id_S2118 |       -6.01038 |
| student_id_S2119 |       -7.14389 |
| student_id_S212  |        0.21447 |

---

### Blocco 109 (Feature 1081 - 1090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2120 |      -6.54097  |
| student_id_S2121 |      -1.76805  |
| student_id_S2122 |       1.81546  |
| student_id_S2124 |      -4.55704  |
| student_id_S2125 |       0.613738 |
| student_id_S2127 |       2.25761  |
| student_id_S2129 |       6.33296  |
| student_id_S213  |      -8.40015  |
| student_id_S2130 |       2.32815  |
| student_id_S2131 |      -3.9292   |

---

### Blocco 110 (Feature 1091 - 1100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2133 |     10.2923    |
| student_id_S2134 |     14.2878    |
| student_id_S2135 |     -0.435502  |
| student_id_S2136 |      2.10321   |
| student_id_S2137 |      4.27589   |
| student_id_S2138 |      8.02048   |
| student_id_S2139 |     -6.08586   |
| student_id_S214  |     -0.0742269 |
| student_id_S2140 |     -1.06143   |
| student_id_S2141 |      4.19037   |

---

### Blocco 111 (Feature 1101 - 1110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2142 |       -5.2806  |
| student_id_S2143 |       -6.75455 |
| student_id_S2145 |        7.02613 |
| student_id_S2147 |       -3.52942 |
| student_id_S2149 |       -6.53043 |
| student_id_S215  |        2.6154  |
| student_id_S2150 |        3.10671 |
| student_id_S2152 |        8.79819 |
| student_id_S2153 |       -8.49731 |
| student_id_S2154 |       -3.14258 |

---

### Blocco 112 (Feature 1111 - 1120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2155 |        7.76795 |
| student_id_S2156 |       11.1597  |
| student_id_S2157 |        2.23282 |
| student_id_S2158 |       -8.2879  |
| student_id_S2159 |        2.42168 |
| student_id_S216  |       -4.75978 |
| student_id_S2160 |       12.0373  |
| student_id_S2161 |       14.1395  |
| student_id_S2162 |        2.06981 |
| student_id_S2163 |        3.03135 |

---

### Blocco 113 (Feature 1121 - 1130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2164 |       3.45316  |
| student_id_S2168 |       0.195446 |
| student_id_S217  |       1.96248  |
| student_id_S2170 |      -2.22326  |
| student_id_S2171 |      11.8176   |
| student_id_S2172 |      -1.34048  |
| student_id_S2173 |       4.71026  |
| student_id_S2176 |       1.90902  |
| student_id_S2177 |       5.20297  |
| student_id_S2179 |       7.02447  |

---

### Blocco 114 (Feature 1131 - 1140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S218  |        2.89472 |
| student_id_S2181 |        8.12765 |
| student_id_S2182 |        3.4203  |
| student_id_S2183 |        6.07864 |
| student_id_S2184 |       -4.31873 |
| student_id_S2186 |      -11.4089  |
| student_id_S2188 |       15.2996  |
| student_id_S2189 |       -4.89649 |
| student_id_S2190 |        3.63092 |
| student_id_S2191 |        1.25897 |

---

### Blocco 115 (Feature 1141 - 1150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2192 |      -6.03444  |
| student_id_S2193 |      -5.89366  |
| student_id_S2194 |      -3.26399  |
| student_id_S2195 |      -3.07505  |
| student_id_S2196 |      16.1995   |
| student_id_S2197 |      12.6186   |
| student_id_S2198 |      -1.15086  |
| student_id_S2199 |       0.649954 |
| student_id_S22   |      14.9442   |
| student_id_S220  |      -7.42383  |

---

### Blocco 116 (Feature 1151 - 1160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2200 |        9.6114  |
| student_id_S2201 |       -5.09782 |
| student_id_S2202 |        3.72795 |
| student_id_S2204 |       -3.04213 |
| student_id_S2205 |        3.89437 |
| student_id_S2206 |        7.40005 |
| student_id_S2207 |        7.86467 |
| student_id_S2208 |       -7.76524 |
| student_id_S2209 |        2.4051  |
| student_id_S2210 |       -7.20069 |

---

### Blocco 117 (Feature 1161 - 1170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2213 |      -3.60705  |
| student_id_S2214 |      -8.06091  |
| student_id_S2217 |      13.419    |
| student_id_S2218 |      -9.42531  |
| student_id_S2219 |       0.516762 |
| student_id_S222  |      -3.58996  |
| student_id_S2221 |       1.33716  |
| student_id_S2222 |      -6.01055  |
| student_id_S2223 |      -8.61144  |
| student_id_S2224 |      -6.5774   |

---

### Blocco 118 (Feature 1171 - 1180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2225 |        2.55361 |
| student_id_S2226 |       -8.16291 |
| student_id_S2227 |        5.51069 |
| student_id_S2228 |        9.68229 |
| student_id_S2229 |        1.84123 |
| student_id_S223  |       -8.17288 |
| student_id_S2230 |        1.84419 |
| student_id_S2231 |       -3.40057 |
| student_id_S2232 |        2.83051 |
| student_id_S2233 |        3.20074 |

---

### Blocco 119 (Feature 1181 - 1190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2234 |      -9.32426  |
| student_id_S2235 |      -2.71307  |
| student_id_S2236 |       5.32202  |
| student_id_S2237 |       7.74587  |
| student_id_S2238 |      11.7834   |
| student_id_S2239 |       0.637949 |
| student_id_S2241 |      -7.60461  |
| student_id_S2242 |      -2.96171  |
| student_id_S2244 |      -3.90793  |
| student_id_S2246 |      -5.37561  |

---

### Blocco 120 (Feature 1191 - 1200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2247 |     -13.8519   |
| student_id_S2248 |       6.15965  |
| student_id_S2249 |       0.880018 |
| student_id_S225  |       6.07697  |
| student_id_S2250 |      -0.052369 |
| student_id_S2251 |      -7.10389  |
| student_id_S2252 |      -7.28884  |
| student_id_S2253 |      -4.80282  |
| student_id_S2254 |      -1.57118  |
| student_id_S2255 |      -4.46187  |

---

### Blocco 121 (Feature 1201 - 1210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2256 |       4.20258  |
| student_id_S2257 |      -0.494414 |
| student_id_S2258 |      -6.64663  |
| student_id_S2259 |      -3.332    |
| student_id_S2260 |      -4.70283  |
| student_id_S2262 |       4.71703  |
| student_id_S2263 |       3.14334  |
| student_id_S2265 |       6.81257  |
| student_id_S2266 |      -2.85099  |
| student_id_S2267 |      -3.62681  |

---

### Blocco 122 (Feature 1211 - 1220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2269 |     -11.0367   |
| student_id_S227  |      -7.63014  |
| student_id_S2270 |       1.64685  |
| student_id_S2271 |      13.9876   |
| student_id_S2272 |       7.6274   |
| student_id_S2275 |     -14.7744   |
| student_id_S2276 |      12.0917   |
| student_id_S2277 |      -3.68926  |
| student_id_S2279 |       0.956964 |
| student_id_S228  |     -12.7576   |

---

### Blocco 123 (Feature 1221 - 1230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2280 |      -4.12748  |
| student_id_S2282 |      -8.84305  |
| student_id_S2283 |      12.3347   |
| student_id_S2284 |      -0.625779 |
| student_id_S2285 |       7.32897  |
| student_id_S2286 |       0.417978 |
| student_id_S2287 |       6.37994  |
| student_id_S229  |       1.63238  |
| student_id_S2291 |     -10.6441   |
| student_id_S2292 |      -6.02213  |

---

### Blocco 124 (Feature 1231 - 1240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2293 |       9.91996  |
| student_id_S2294 |      -3.94665  |
| student_id_S2295 |       1.21301  |
| student_id_S2297 |      -0.312779 |
| student_id_S2299 |      12.9849   |
| student_id_S23   |       7.61946  |
| student_id_S230  |       0.11777  |
| student_id_S2300 |      -6.29984  |
| student_id_S2301 |      -7.28495  |
| student_id_S2302 |       5.45178  |

---

### Blocco 125 (Feature 1241 - 1250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2304 |      16.524    |
| student_id_S2305 |       5.77423  |
| student_id_S2306 |      -1.8096   |
| student_id_S2308 |       3.73066  |
| student_id_S2309 |      -5.52078  |
| student_id_S231  |      -7.22037  |
| student_id_S2310 |       5.23479  |
| student_id_S2311 |      -2.05153  |
| student_id_S2312 |      -0.199069 |
| student_id_S2313 |      12.111    |

---

### Blocco 126 (Feature 1251 - 1260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2314 |        6.44211 |
| student_id_S2315 |       -2.46713 |
| student_id_S2316 |       -8.94542 |
| student_id_S2319 |      -12.4594  |
| student_id_S232  |       10.263   |
| student_id_S2320 |        2.86426 |
| student_id_S2321 |       10.3639  |
| student_id_S2324 |      -10.1883  |
| student_id_S2325 |       -9.10124 |
| student_id_S2327 |       -5.60002 |

---

### Blocco 127 (Feature 1261 - 1270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2328 |     11.871     |
| student_id_S233  |     -5.68668   |
| student_id_S2330 |     13.8643    |
| student_id_S2331 |     -3.75903   |
| student_id_S2332 |     16.7291    |
| student_id_S2333 |     -0.0797239 |
| student_id_S2334 |      0.851864  |
| student_id_S2335 |      5.67602   |
| student_id_S2336 |      0.205279  |
| student_id_S2337 |     15.8178    |

---

### Blocco 128 (Feature 1271 - 1280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2338 |        0.33283 |
| student_id_S2339 |        2.74677 |
| student_id_S234  |       -6.50564 |
| student_id_S2340 |       -2.10424 |
| student_id_S2341 |       -6.72442 |
| student_id_S2343 |       -6.15932 |
| student_id_S2344 |       -5.60323 |
| student_id_S2345 |       -6.93367 |
| student_id_S2347 |       -2.45253 |
| student_id_S2349 |       10.5181  |

---

### Blocco 129 (Feature 1281 - 1290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S235  |        9.87467 |
| student_id_S2350 |        6.14238 |
| student_id_S2351 |        6.29439 |
| student_id_S2352 |       10.3166  |
| student_id_S2353 |       -2.74575 |
| student_id_S2354 |       -1.76034 |
| student_id_S2355 |        9.23063 |
| student_id_S2357 |       15.8415  |
| student_id_S2358 |       -4.71635 |
| student_id_S2359 |        1.46349 |

---

### Blocco 130 (Feature 1291 - 1300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2362 |       6.24221  |
| student_id_S2364 |       1.11604  |
| student_id_S2365 |       5.49587  |
| student_id_S2366 |       3.25731  |
| student_id_S2367 |      -2.46668  |
| student_id_S2368 |       6.3215   |
| student_id_S2369 |       0.313343 |
| student_id_S237  |      -3.25218  |
| student_id_S2370 |       2.36131  |
| student_id_S2371 |      -4.9244   |

---

### Blocco 131 (Feature 1301 - 1310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2372 |       -1.1609  |
| student_id_S2374 |        6.593   |
| student_id_S2375 |       -7.57438 |
| student_id_S2376 |        4.51186 |
| student_id_S2378 |        4.39608 |
| student_id_S2379 |        0.52915 |
| student_id_S238  |        3.32195 |
| student_id_S2380 |        3.68341 |
| student_id_S2381 |       13.8882  |
| student_id_S2382 |       -0.16204 |

---

### Blocco 132 (Feature 1311 - 1320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2383 |      -4.20391  |
| student_id_S2384 |      -3.15345  |
| student_id_S2386 |      -5.02071  |
| student_id_S2387 |      -7.38927  |
| student_id_S2388 |       0.189386 |
| student_id_S239  |       2.56031  |
| student_id_S2391 |      -5.66439  |
| student_id_S2392 |       0.839465 |
| student_id_S2393 |      -6.53254  |
| student_id_S2394 |      -8.61311  |

---

### Blocco 133 (Feature 1321 - 1330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2395 |       -8.91792 |
| student_id_S2398 |        3.09793 |
| student_id_S24   |       -8.35968 |
| student_id_S240  |       -5.75839 |
| student_id_S2400 |       11.0694  |
| student_id_S2401 |       -8.61952 |
| student_id_S2402 |       -2.9991  |
| student_id_S2403 |        6.81451 |
| student_id_S2405 |        1.19464 |
| student_id_S2406 |        7.03104 |

---

### Blocco 134 (Feature 1331 - 1340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2407 |       0.867954 |
| student_id_S2408 |      12.4217   |
| student_id_S2409 |      -8.36879  |
| student_id_S241  |       3.14665  |
| student_id_S2410 |      -3.65344  |
| student_id_S2411 |     -11.678    |
| student_id_S2413 |      -3.5126   |
| student_id_S2414 |       6.48838  |
| student_id_S2415 |      -9.53871  |
| student_id_S2416 |      -6.93087  |

---

### Blocco 135 (Feature 1341 - 1350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2417 |      -5.21304  |
| student_id_S2418 |      -3.13184  |
| student_id_S2419 |      -0.557557 |
| student_id_S242  |       6.12316  |
| student_id_S2420 |       3.94946  |
| student_id_S2421 |      -2.06756  |
| student_id_S2422 |       6.78861  |
| student_id_S2423 |      11.6995   |
| student_id_S2424 |      -0.250168 |
| student_id_S2425 |      -2.19472  |

---

### Blocco 136 (Feature 1351 - 1360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2426 |       10.5331  |
| student_id_S2427 |       -4.476   |
| student_id_S2428 |       -1.0756  |
| student_id_S243  |        2.14984 |
| student_id_S2431 |      -11.3934  |
| student_id_S2432 |       15.2105  |
| student_id_S2433 |       -5.75567 |
| student_id_S2434 |       -1.68267 |
| student_id_S2435 |        6.24863 |
| student_id_S2437 |      -12.2762  |

---

### Blocco 137 (Feature 1361 - 1370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2439 |        3.77964 |
| student_id_S244  |        1.92554 |
| student_id_S2440 |       -4.53432 |
| student_id_S2441 |       -5.01816 |
| student_id_S2442 |        6.22984 |
| student_id_S2443 |       15.756   |
| student_id_S2444 |        4.48368 |
| student_id_S2446 |        1.19971 |
| student_id_S2447 |      -11.2937  |
| student_id_S2448 |       -3.38707 |

---

### Blocco 138 (Feature 1371 - 1380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2449 |       7.94059  |
| student_id_S2451 |       3.79871  |
| student_id_S2452 |      -5.87805  |
| student_id_S2453 |       0.107895 |
| student_id_S2455 |      -0.148165 |
| student_id_S2456 |     -12.3734   |
| student_id_S2457 |      -5.87814  |
| student_id_S2458 |      -0.592294 |
| student_id_S2459 |      -2.08397  |
| student_id_S246  |      -8.50045  |

---

### Blocco 139 (Feature 1381 - 1390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2460 |        3.46382 |
| student_id_S2461 |      -12.2479  |
| student_id_S2462 |       -9.68574 |
| student_id_S2463 |        6.09649 |
| student_id_S2465 |        8.203   |
| student_id_S2466 |        5.72381 |
| student_id_S2467 |        4.08025 |
| student_id_S2468 |       -2.26216 |
| student_id_S2469 |       -8.21439 |
| student_id_S247  |        2.50117 |

---

### Blocco 140 (Feature 1391 - 1400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2471 |      -3.26336  |
| student_id_S2472 |       0.839722 |
| student_id_S2473 |      -2.43786  |
| student_id_S2474 |      -7.53474  |
| student_id_S2475 |       2.06877  |
| student_id_S2476 |       3.32813  |
| student_id_S2477 |       8.87935  |
| student_id_S2478 |       7.31695  |
| student_id_S2479 |       0.135937 |
| student_id_S248  |      -5.53691  |

---

### Blocco 141 (Feature 1401 - 1410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2480 |       -2.80017 |
| student_id_S2481 |       -9.80862 |
| student_id_S2484 |        2.73309 |
| student_id_S2486 |       -4.29243 |
| student_id_S2487 |        8.08762 |
| student_id_S2488 |        9.81047 |
| student_id_S2489 |       11.8661  |
| student_id_S249  |       -8.46913 |
| student_id_S2490 |       -2.55195 |
| student_id_S2491 |        3.62605 |

---

### Blocco 142 (Feature 1411 - 1420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2492 |        6.43661 |
| student_id_S2493 |        5.79682 |
| student_id_S2495 |       -5.1084  |
| student_id_S2496 |        6.74515 |
| student_id_S2497 |       -7.12839 |
| student_id_S2498 |        5.48513 |
| student_id_S25   |        5.8512  |
| student_id_S250  |        2.70293 |
| student_id_S2500 |        6.63504 |
| student_id_S2501 |       10.6384  |

---

### Blocco 143 (Feature 1421 - 1430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2502 |      -0.708242 |
| student_id_S2503 |      12.5383   |
| student_id_S2504 |      -5.46422  |
| student_id_S2505 |      -0.327176 |
| student_id_S2506 |       0.356616 |
| student_id_S2507 |      -6.09588  |
| student_id_S2508 |      -5.93465  |
| student_id_S2509 |       6.58113  |
| student_id_S251  |       3.18394  |
| student_id_S2510 |      -4.64182  |

---

### Blocco 144 (Feature 1431 - 1440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2511 |       -5.83938 |
| student_id_S2512 |       -5.12254 |
| student_id_S2513 |        9.26697 |
| student_id_S2514 |       -8.41207 |
| student_id_S2515 |        3.63707 |
| student_id_S2517 |        8.59577 |
| student_id_S2518 |        5.02815 |
| student_id_S2519 |       -4.01571 |
| student_id_S252  |       -3.05423 |
| student_id_S2521 |       -4.2572  |

---

### Blocco 145 (Feature 1441 - 1450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2522 |       -6.84663 |
| student_id_S2523 |       -2.19093 |
| student_id_S2525 |       -4.52854 |
| student_id_S2526 |        1.98378 |
| student_id_S2527 |        4.71698 |
| student_id_S2529 |       -6.87281 |
| student_id_S2530 |       10.0281  |
| student_id_S2531 |       -9.96014 |
| student_id_S2532 |       -9.99317 |
| student_id_S2534 |        3.33739 |

---

### Blocco 146 (Feature 1451 - 1460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2535 |       -3.4101  |
| student_id_S2538 |       15.6909  |
| student_id_S254  |      -13.9978  |
| student_id_S2540 |       -2.39769 |
| student_id_S2541 |        8.95416 |
| student_id_S2542 |        5.979   |
| student_id_S2544 |       11.2806  |
| student_id_S2545 |       -2.29722 |
| student_id_S2546 |       -7.12169 |
| student_id_S2547 |       10.4068  |

---

### Blocco 147 (Feature 1461 - 1470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2548 |      -14.5513  |
| student_id_S2549 |       -6.37489 |
| student_id_S255  |       -6.26339 |
| student_id_S2551 |       -2.31589 |
| student_id_S2553 |       -6.79928 |
| student_id_S2554 |        5.73074 |
| student_id_S2555 |       10.6289  |
| student_id_S2556 |       -2.64561 |
| student_id_S2558 |       -5.38922 |
| student_id_S2559 |       -4.74165 |

---

### Blocco 148 (Feature 1471 - 1480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S256  |      16.9621   |
| student_id_S2560 |       6.84111  |
| student_id_S2561 |       1.05151  |
| student_id_S2564 |       2.73621  |
| student_id_S2565 |       9.7981   |
| student_id_S2566 |      -0.649073 |
| student_id_S2567 |       1.22352  |
| student_id_S257  |      -2.30289  |
| student_id_S2570 |       4.70142  |
| student_id_S2571 |       0.802254 |

---

### Blocco 149 (Feature 1481 - 1490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2572 |      0.0277126 |
| student_id_S2573 |      9.67206   |
| student_id_S2574 |      3.17534   |
| student_id_S2575 |    -12.5664    |
| student_id_S2577 |     -2.61144   |
| student_id_S2578 |     -5.55647   |
| student_id_S2579 |     -9.64639   |
| student_id_S258  |      1.25176   |
| student_id_S2580 |      4.99663   |
| student_id_S2581 |      5.05545   |

---

### Blocco 150 (Feature 1491 - 1500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2583 |      -0.43536  |
| student_id_S2584 |       3.23155  |
| student_id_S2585 |       7.40346  |
| student_id_S2586 |       1.28242  |
| student_id_S2587 |      10.3074   |
| student_id_S2588 |       8.08344  |
| student_id_S2589 |      -0.334324 |
| student_id_S259  |       1.79451  |
| student_id_S2590 |      -1.73049  |
| student_id_S2591 |       3.51651  |

---

### Blocco 151 (Feature 1501 - 1510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2592 |       3.09469  |
| student_id_S2593 |      -0.824319 |
| student_id_S2595 |      -2.15896  |
| student_id_S2596 |      -3.55444  |
| student_id_S2597 |       2.42879  |
| student_id_S2598 |       4.38229  |
| student_id_S2599 |       3.83656  |
| student_id_S26   |     -12.0249   |
| student_id_S260  |       0.517099 |
| student_id_S2600 |      13.7287   |

---

### Blocco 152 (Feature 1511 - 1520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2601 |       6.17449  |
| student_id_S2602 |      -3.31664  |
| student_id_S2604 |      -9.45582  |
| student_id_S2606 |       4.29742  |
| student_id_S2607 |      17.9291   |
| student_id_S2608 |      -3.59142  |
| student_id_S2609 |       8.6804   |
| student_id_S261  |      -5.17321  |
| student_id_S2610 |       0.241406 |
| student_id_S2611 |       1.40197  |

---

### Blocco 153 (Feature 1521 - 1530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2612 |        8.15412 |
| student_id_S2614 |        7.48015 |
| student_id_S2615 |        8.29737 |
| student_id_S2616 |       -1.98238 |
| student_id_S2617 |       13.998   |
| student_id_S2618 |        2.25055 |
| student_id_S2619 |        7.26593 |
| student_id_S262  |       -2.77382 |
| student_id_S2620 |        6.48843 |
| student_id_S2621 |       -5.42255 |

---

### Blocco 154 (Feature 1531 - 1540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2622 |      -4.43309  |
| student_id_S2623 |       0.778771 |
| student_id_S2624 |       1.77017  |
| student_id_S2625 |       1.15362  |
| student_id_S2626 |       4.11307  |
| student_id_S2627 |      -6.03063  |
| student_id_S2628 |      -2.2117   |
| student_id_S2629 |      -8.19751  |
| student_id_S263  |      -1.52252  |
| student_id_S2630 |      -9.7023   |

---

### Blocco 155 (Feature 1541 - 1550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2631 |       -2.78167 |
| student_id_S2633 |        5.50757 |
| student_id_S2634 |        5.67491 |
| student_id_S2635 |       -6.63449 |
| student_id_S2638 |       -9.18366 |
| student_id_S2639 |        4.5781  |
| student_id_S264  |       -7.22607 |
| student_id_S2641 |       -7.13458 |
| student_id_S2642 |        7.74658 |
| student_id_S2643 |        2.16245 |

---

### Blocco 156 (Feature 1551 - 1560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2644 |       -0.76403 |
| student_id_S2645 |       -1.76337 |
| student_id_S2646 |        1.8308  |
| student_id_S2647 |       -2.59482 |
| student_id_S2648 |       -9.48529 |
| student_id_S2649 |       16.4992  |
| student_id_S265  |       -2.42816 |
| student_id_S2651 |        5.75735 |
| student_id_S2652 |        9.49434 |
| student_id_S2653 |       12.7451  |

---

### Blocco 157 (Feature 1561 - 1570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2654 |      -0.889502 |
| student_id_S2655 |       1.2701   |
| student_id_S2656 |     -10.6723   |
| student_id_S2657 |      16.995    |
| student_id_S2658 |      -7.94824  |
| student_id_S2659 |     -10.3501   |
| student_id_S2661 |      -3.47638  |
| student_id_S2662 |      12.516    |
| student_id_S2663 |       9.25445  |
| student_id_S2664 |      10.873    |

---

### Blocco 158 (Feature 1571 - 1580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2665 |       16.2744  |
| student_id_S2666 |       -4.27827 |
| student_id_S2669 |       -3.37937 |
| student_id_S267  |       -3.99005 |
| student_id_S2670 |       -7.6056  |
| student_id_S2671 |       -7.93812 |
| student_id_S2672 |        3.25066 |
| student_id_S2673 |        5.60879 |
| student_id_S2674 |       -3.69614 |
| student_id_S2675 |        1.62501 |

---

### Blocco 159 (Feature 1581 - 1590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2676 |        9.26682 |
| student_id_S2677 |      -15.3497  |
| student_id_S2678 |       -1.67311 |
| student_id_S2679 |       -8.13637 |
| student_id_S268  |       -2.68197 |
| student_id_S2680 |       -2.08865 |
| student_id_S2681 |        8.00672 |
| student_id_S2683 |      -12.7971  |
| student_id_S2684 |      -17.6314  |
| student_id_S2685 |       -4.76524 |

---

### Blocco 160 (Feature 1591 - 1600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2686 |      -0.395129 |
| student_id_S2687 |       7.66542  |
| student_id_S2688 |       5.41323  |
| student_id_S2689 |       1.88205  |
| student_id_S269  |      -8.84443  |
| student_id_S2690 |       1.50983  |
| student_id_S2692 |      12.3116   |
| student_id_S2693 |       1.15951  |
| student_id_S2694 |      -3.9339   |
| student_id_S2695 |       8.37461  |

---

### Blocco 161 (Feature 1601 - 1610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2696 |       11.9719  |
| student_id_S2697 |       -6.79418 |
| student_id_S2698 |        4.05287 |
| student_id_S2699 |       -1.71053 |
| student_id_S27   |        6.53631 |
| student_id_S2700 |        3.84183 |
| student_id_S2701 |        4.97166 |
| student_id_S2702 |        9.16231 |
| student_id_S2703 |        1.53566 |
| student_id_S2704 |        2.99667 |

---

### Blocco 162 (Feature 1611 - 1620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2705 |       11.4835  |
| student_id_S2706 |       -5.45688 |
| student_id_S2708 |       -5.13113 |
| student_id_S2709 |       -1.57839 |
| student_id_S271  |       10.3062  |
| student_id_S2711 |       11.8329  |
| student_id_S2712 |        7.07335 |
| student_id_S2713 |        4.86014 |
| student_id_S2714 |       11.3652  |
| student_id_S2715 |      -11.9927  |

---

### Blocco 163 (Feature 1621 - 1630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2716 |      -7.6232   |
| student_id_S2717 |      11.7767   |
| student_id_S2718 |      -0.879744 |
| student_id_S2719 |      12.8084   |
| student_id_S272  |       3.51751  |
| student_id_S2720 |      -1.33197  |
| student_id_S2721 |      -7.94793  |
| student_id_S2723 |      -0.407677 |
| student_id_S2724 |      -4.20761  |
| student_id_S2725 |      -3.0794   |

---

### Blocco 164 (Feature 1631 - 1640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2726 |      3.6836    |
| student_id_S2727 |      0.463909  |
| student_id_S2728 |     -5.31411   |
| student_id_S2729 |      1.11719   |
| student_id_S273  |      0.551399  |
| student_id_S2730 |     -2.84049   |
| student_id_S2732 |      0.0167144 |
| student_id_S2733 |      0.0352445 |
| student_id_S2734 |     16.2935    |
| student_id_S2735 |      1.74368   |

---

### Blocco 165 (Feature 1641 - 1650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2736 |       5.43983  |
| student_id_S2738 |      -3.68174  |
| student_id_S2739 |      -4.06111  |
| student_id_S274  |       2.36972  |
| student_id_S2740 |       0.252026 |
| student_id_S2741 |       8.20715  |
| student_id_S2742 |       7.03075  |
| student_id_S2743 |       2.69705  |
| student_id_S2744 |      -2.3987   |
| student_id_S2746 |      -6.17338  |

---

### Blocco 166 (Feature 1651 - 1660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2747 |       11.4033  |
| student_id_S2748 |      -13.2069  |
| student_id_S2749 |       -1.65509 |
| student_id_S275  |       13.1997  |
| student_id_S2750 |       -6.04672 |
| student_id_S2751 |        3.57051 |
| student_id_S2752 |       -5.41641 |
| student_id_S2754 |        1.3354  |
| student_id_S2755 |       -2.55853 |
| student_id_S2756 |        1.94999 |

---

### Blocco 167 (Feature 1661 - 1670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2757 |       4.7722   |
| student_id_S2758 |       8.3454   |
| student_id_S276  |     -10.6017   |
| student_id_S2761 |       0.747782 |
| student_id_S2762 |      17.4572   |
| student_id_S2763 |     -12.8177   |
| student_id_S2764 |       4.39588  |
| student_id_S2765 |      -4.75079  |
| student_id_S2766 |       5.65849  |
| student_id_S2768 |       5.74106  |

---

### Blocco 168 (Feature 1671 - 1680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2769 |      -7.53813  |
| student_id_S277  |     -10.1389   |
| student_id_S2770 |       9.85877  |
| student_id_S2771 |       0.22742  |
| student_id_S2772 |      -0.410408 |
| student_id_S2773 |      14.1841   |
| student_id_S2774 |      -3.94538  |
| student_id_S2776 |      -8.3099   |
| student_id_S2777 |       9.88239  |
| student_id_S2778 |       7.91908  |

---

### Blocco 169 (Feature 1681 - 1690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2779 |       2.74389  |
| student_id_S278  |      -5.22608  |
| student_id_S2780 |       4.1282   |
| student_id_S2782 |      16.0266   |
| student_id_S2783 |       1.68129  |
| student_id_S2784 |      -0.592584 |
| student_id_S2785 |       1.37054  |
| student_id_S2786 |      -0.720937 |
| student_id_S2787 |      10.9324   |
| student_id_S2788 |       3.37324  |

---

### Blocco 170 (Feature 1691 - 1700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2789 |        2.39761 |
| student_id_S279  |        7.07519 |
| student_id_S2790 |        8.82909 |
| student_id_S2791 |        5.32443 |
| student_id_S2792 |       10.8572  |
| student_id_S2793 |       -6.00591 |
| student_id_S2794 |        5.56783 |
| student_id_S2796 |       -2.09478 |
| student_id_S2797 |      -13.7757  |
| student_id_S2798 |       -2.8464  |

---

### Blocco 171 (Feature 1701 - 1710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2799 |       2.77041  |
| student_id_S28   |      -7.2673   |
| student_id_S280  |       2.33281  |
| student_id_S2800 |       3.58927  |
| student_id_S2801 |      -9.82452  |
| student_id_S2802 |      -7.5058   |
| student_id_S2803 |      -0.850309 |
| student_id_S2804 |       1.43157  |
| student_id_S2805 |      10.7437   |
| student_id_S2806 |     -12.6009   |

---

### Blocco 172 (Feature 1711 - 1720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2807 |      12.745    |
| student_id_S2808 |       3.44235  |
| student_id_S2809 |      -4.14282  |
| student_id_S281  |       0.683087 |
| student_id_S2810 |      11.0378   |
| student_id_S2811 |      -4.58122  |
| student_id_S2812 |       4.36259  |
| student_id_S2813 |      10.4686   |
| student_id_S2814 |      -1.79449  |
| student_id_S2815 |      -5.74495  |

---

### Blocco 173 (Feature 1721 - 1730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2818 |     -0.0944863 |
| student_id_S2819 |      7.12989   |
| student_id_S2820 |     14.1731    |
| student_id_S2821 |     -1.2414    |
| student_id_S2822 |     -3.49278   |
| student_id_S2823 |     -2.47756   |
| student_id_S2824 |     -9.12313   |
| student_id_S2825 |      5.08876   |
| student_id_S2826 |      6.09472   |
| student_id_S2827 |     -3.34132   |

---

### Blocco 174 (Feature 1731 - 1740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2828 |       3.74506  |
| student_id_S2829 |      11.4348   |
| student_id_S283  |      -5.54103  |
| student_id_S2830 |      -0.532188 |
| student_id_S2831 |       2.92522  |
| student_id_S2832 |      10.4968   |
| student_id_S2833 |      -5.36232  |
| student_id_S2834 |       3.87337  |
| student_id_S2835 |      16.9335   |
| student_id_S2836 |     -16.7015   |

---

### Blocco 175 (Feature 1741 - 1750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2837 |      -16.1076  |
| student_id_S2838 |        1.89042 |
| student_id_S284  |       -6.70062 |
| student_id_S2840 |        1.10067 |
| student_id_S2841 |        3.11975 |
| student_id_S2842 |       16.5877  |
| student_id_S2843 |       -3.4834  |
| student_id_S2844 |      -11.9243  |
| student_id_S2845 |        4.17896 |
| student_id_S2846 |       -6.4002  |

---

### Blocco 176 (Feature 1751 - 1760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2849 |       4.56339  |
| student_id_S285  |       4.51013  |
| student_id_S2850 |       7.25192  |
| student_id_S2851 |      15.7384   |
| student_id_S2852 |      -0.833218 |
| student_id_S2853 |       5.10227  |
| student_id_S2854 |       3.29673  |
| student_id_S2855 |      -0.334081 |
| student_id_S2856 |       0.336003 |
| student_id_S2857 |      13.4559   |

---

### Blocco 177 (Feature 1761 - 1770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2858 |      -0.348949 |
| student_id_S2859 |      -9.35199  |
| student_id_S2860 |       0.94401  |
| student_id_S2861 |      -5.29567  |
| student_id_S2862 |     -13.1572   |
| student_id_S2863 |       3.66478  |
| student_id_S2864 |      -3.6308   |
| student_id_S2865 |      -3.37067  |
| student_id_S2866 |       8.79034  |
| student_id_S2867 |       1.63074  |

---

### Blocco 178 (Feature 1771 - 1780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2869 |       -4.79733 |
| student_id_S2870 |        6.77973 |
| student_id_S2872 |        8.53119 |
| student_id_S2873 |        1.15634 |
| student_id_S2875 |       -7.4903  |
| student_id_S2876 |       -5.25812 |
| student_id_S2877 |      -12.0469  |
| student_id_S2879 |        1.52993 |
| student_id_S288  |       -6.08812 |
| student_id_S2880 |       10.4406  |

---

### Blocco 179 (Feature 1781 - 1790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2881 |       3.15273  |
| student_id_S2882 |      -2.29369  |
| student_id_S2883 |      -8.09122  |
| student_id_S2884 |       4.50891  |
| student_id_S2885 |      -4.63396  |
| student_id_S2886 |       3.74559  |
| student_id_S2887 |       4.64951  |
| student_id_S2889 |      -0.204327 |
| student_id_S289  |     -11.3123   |
| student_id_S2890 |     -11.6195   |

---

### Blocco 180 (Feature 1791 - 1800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2891 |       -0.85451 |
| student_id_S2892 |       -2.0751  |
| student_id_S2893 |       10.1509  |
| student_id_S2894 |        2.67173 |
| student_id_S2895 |       -4.29658 |
| student_id_S2896 |      -12.4954  |
| student_id_S2897 |       -4.60761 |
| student_id_S2898 |        2.18799 |
| student_id_S29   |       -4.57531 |
| student_id_S290  |        1.84661 |

---

### Blocco 181 (Feature 1801 - 1810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2900 |       -1.21413 |
| student_id_S2901 |        4.21598 |
| student_id_S2902 |        4.03126 |
| student_id_S2904 |       -7.58208 |
| student_id_S2905 |       -4.4776  |
| student_id_S2906 |        9.61791 |
| student_id_S2909 |        6.49376 |
| student_id_S291  |        1.09205 |
| student_id_S2910 |       -6.87403 |
| student_id_S2911 |       -2.1199  |

---

### Blocco 182 (Feature 1811 - 1820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2913 |       4.61287  |
| student_id_S2914 |      -5.37111  |
| student_id_S2916 |      11.3617   |
| student_id_S2917 |      -3.11316  |
| student_id_S2918 |      12.1766   |
| student_id_S2919 |       5.74734  |
| student_id_S292  |      -0.169319 |
| student_id_S2920 |      -2.5638   |
| student_id_S2921 |      -9.84238  |
| student_id_S2922 |      -1.36152  |

---

### Blocco 183 (Feature 1821 - 1830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2923 |      -12.7656  |
| student_id_S2924 |       -5.92593 |
| student_id_S2925 |       -3.81132 |
| student_id_S2926 |       -8.31153 |
| student_id_S2927 |        4.69897 |
| student_id_S2928 |        7.87878 |
| student_id_S2929 |       -8.83858 |
| student_id_S2930 |       -6.68545 |
| student_id_S2932 |       -5.16038 |
| student_id_S2933 |        5.32026 |

---

### Blocco 184 (Feature 1831 - 1840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2934 |       3.38551  |
| student_id_S2935 |      -0.532965 |
| student_id_S2936 |      -0.154929 |
| student_id_S2937 |      -2.0919   |
| student_id_S2938 |       6.17663  |
| student_id_S2939 |      -8.83416  |
| student_id_S294  |       0.493803 |
| student_id_S2940 |       2.29756  |
| student_id_S2941 |     -10.1077   |
| student_id_S2944 |       1.94609  |

---

### Blocco 185 (Feature 1841 - 1850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2945 |        2.22694 |
| student_id_S2946 |        3.99827 |
| student_id_S2947 |        2.48922 |
| student_id_S2948 |       -6.34958 |
| student_id_S2949 |       10.333   |
| student_id_S295  |        6.0102  |
| student_id_S2951 |       -5.04091 |
| student_id_S2953 |       -5.80085 |
| student_id_S2954 |       -7.94478 |
| student_id_S2955 |       -8.83429 |

---

### Blocco 186 (Feature 1851 - 1860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2956 |      12.2661   |
| student_id_S2957 |     -15.5233   |
| student_id_S2958 |     -13.2704   |
| student_id_S2959 |      -4.74228  |
| student_id_S296  |       2.45868  |
| student_id_S2960 |      -2.31286  |
| student_id_S2964 |      -1.06036  |
| student_id_S2965 |       1.34982  |
| student_id_S2966 |      -3.41774  |
| student_id_S2967 |       0.211027 |

---

### Blocco 187 (Feature 1861 - 1870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S2968 |      -6.02979  |
| student_id_S2969 |      -0.458004 |
| student_id_S297  |      -2.53973  |
| student_id_S2971 |      -1.39453  |
| student_id_S2972 |       6.07513  |
| student_id_S2973 |      -5.99555  |
| student_id_S2975 |      -2.87929  |
| student_id_S2977 |       6.85841  |
| student_id_S2978 |      -8.61925  |
| student_id_S2979 |      -8.61912  |

---

### Blocco 188 (Feature 1871 - 1880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S298  |      -3.75195  |
| student_id_S2980 |      -6.70998  |
| student_id_S2981 |       2.71156  |
| student_id_S2982 |      -6.86612  |
| student_id_S2983 |      -0.829085 |
| student_id_S2984 |       1.64211  |
| student_id_S2985 |      -8.28364  |
| student_id_S2986 |       7.19793  |
| student_id_S2988 |      -5.80354  |
| student_id_S2989 |      -1.44221  |

---

### Blocco 189 (Feature 1881 - 1890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S299  |     -9.97001   |
| student_id_S2990 |     -2.5359    |
| student_id_S2991 |     -5.79409   |
| student_id_S2992 |     -1.24152   |
| student_id_S2993 |     -0.914236  |
| student_id_S2994 |      2.32297   |
| student_id_S2995 |      4.65165   |
| student_id_S2997 |      8.32993   |
| student_id_S2998 |      1.58015   |
| student_id_S2999 |     -0.0506291 |

---

### Blocco 190 (Feature 1891 - 1900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3    |       -2.17891 |
| student_id_S30   |       -8.01638 |
| student_id_S300  |        4.37131 |
| student_id_S3000 |       -1.09278 |
| student_id_S3001 |        9.28491 |
| student_id_S3002 |        1.35051 |
| student_id_S3003 |        5.15713 |
| student_id_S3004 |        1.04098 |
| student_id_S3005 |        2.65501 |
| student_id_S3006 |       -5.8225  |

---

### Blocco 191 (Feature 1901 - 1910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3007 |        5.24972 |
| student_id_S3008 |        2.64481 |
| student_id_S3009 |       -8.65853 |
| student_id_S3010 |        2.99125 |
| student_id_S3011 |       -9.24706 |
| student_id_S3012 |      -10.816   |
| student_id_S3014 |       -1.72927 |
| student_id_S3015 |       -7.07946 |
| student_id_S3016 |        6.56537 |
| student_id_S3017 |       11.3213  |

---

### Blocco 192 (Feature 1911 - 1920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3018 |      -0.508333 |
| student_id_S3019 |       8.43333  |
| student_id_S302  |       2.41081  |
| student_id_S3020 |      -8.23357  |
| student_id_S3021 |       7.48044  |
| student_id_S3022 |      -2.2497   |
| student_id_S3023 |      -7.36087  |
| student_id_S3024 |      -1.89348  |
| student_id_S3025 |      -2.21911  |
| student_id_S3026 |      11.5821   |

---

### Blocco 193 (Feature 1921 - 1930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3027 |       5.41007  |
| student_id_S3028 |     -11.3181   |
| student_id_S3029 |       6.3706   |
| student_id_S303  |       2.53359  |
| student_id_S3030 |      -3.22759  |
| student_id_S3031 |      -2.69873  |
| student_id_S3032 |       0.864618 |
| student_id_S3033 |      11.1011   |
| student_id_S3034 |      -9.99767  |
| student_id_S3035 |      -1.34746  |

---

### Blocco 194 (Feature 1931 - 1940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3036 |      -7.35353  |
| student_id_S3037 |      -8.95088  |
| student_id_S3038 |      13.9455   |
| student_id_S3039 |       0.579302 |
| student_id_S304  |      -2.6158   |
| student_id_S3040 |      11.7351   |
| student_id_S3041 |      -0.259591 |
| student_id_S3043 |      -5.96141  |
| student_id_S3044 |       6.46553  |
| student_id_S3045 |      -9.42186  |

---

### Blocco 195 (Feature 1941 - 1950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3046 |     -1.03435   |
| student_id_S3047 |    -15.0661    |
| student_id_S3048 |     -2.60062   |
| student_id_S3049 |      9.34509   |
| student_id_S305  |     -7.80784   |
| student_id_S3050 |     11.3597    |
| student_id_S3051 |      5.5944    |
| student_id_S3052 |     -3.04003   |
| student_id_S3053 |      0.0847152 |
| student_id_S3054 |    -11.2613    |

---

### Blocco 196 (Feature 1951 - 1960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3055 |       -2.31933 |
| student_id_S3056 |       -6.14481 |
| student_id_S3058 |       -6.60915 |
| student_id_S3059 |        1.68775 |
| student_id_S306  |        4.20637 |
| student_id_S3060 |      -10.7014  |
| student_id_S3061 |        2.13924 |
| student_id_S3062 |       11.5707  |
| student_id_S3063 |        4.42535 |
| student_id_S3064 |        9.39703 |

---

### Blocco 197 (Feature 1961 - 1970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3065 |     -13.7487   |
| student_id_S3066 |      -0.649763 |
| student_id_S3067 |     -13.0011   |
| student_id_S3068 |      -1.41971  |
| student_id_S307  |       3.26397  |
| student_id_S3070 |      -1.80715  |
| student_id_S3071 |      -3.16122  |
| student_id_S3072 |       5.65864  |
| student_id_S3073 |       1.06995  |
| student_id_S3075 |       6.38269  |

---

### Blocco 198 (Feature 1971 - 1980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3076 |       -1.86893 |
| student_id_S3077 |       -1.88006 |
| student_id_S3078 |       -1.52237 |
| student_id_S308  |       -2.55954 |
| student_id_S3080 |       -2.31285 |
| student_id_S3081 |       -7.26738 |
| student_id_S3082 |       12.23    |
| student_id_S3083 |        8.74923 |
| student_id_S3084 |        7.84753 |
| student_id_S3086 |       -1.09423 |

---

### Blocco 199 (Feature 1981 - 1990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3087 |       2.1558   |
| student_id_S3089 |       5.19211  |
| student_id_S309  |      -4.83716  |
| student_id_S3090 |       1.34961  |
| student_id_S3092 |       1.9279   |
| student_id_S3093 |       3.30179  |
| student_id_S3094 |      12.6045   |
| student_id_S3095 |       0.63064  |
| student_id_S3096 |      11.3082   |
| student_id_S3097 |      -0.122713 |

---

### Blocco 200 (Feature 1991 - 2000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3098 |      1.1615    |
| student_id_S3099 |     -0.0103233 |
| student_id_S31   |     -7.97509   |
| student_id_S310  |      2.64085   |
| student_id_S3101 |     -2.75623   |
| student_id_S3102 |     -7.2899    |
| student_id_S3103 |     -4.85602   |
| student_id_S3104 |      6.0288    |
| student_id_S3105 |     -1.43695   |
| student_id_S3106 |     11.7359    |

---

### Blocco 201 (Feature 2001 - 2010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3107 |      -0.801202 |
| student_id_S3108 |      -2.36943  |
| student_id_S3109 |      -2.70852  |
| student_id_S311  |      -7.03415  |
| student_id_S3110 |      -5.09035  |
| student_id_S3111 |      -7.07601  |
| student_id_S3112 |       9.21526  |
| student_id_S3113 |      -5.0454   |
| student_id_S3114 |       2.28352  |
| student_id_S3115 |       0.558283 |

---

### Blocco 202 (Feature 2011 - 2020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3116 |     -10.472    |
| student_id_S3117 |       3.88038  |
| student_id_S3119 |       2.70269  |
| student_id_S312  |      -8.67445  |
| student_id_S3122 |      -8.0009   |
| student_id_S3123 |      -2.69348  |
| student_id_S3124 |       0.839945 |
| student_id_S3125 |      -7.56034  |
| student_id_S3127 |      -7.72117  |
| student_id_S3128 |      -1.32534  |

---

### Blocco 203 (Feature 2021 - 2030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3129 |      -9.49067  |
| student_id_S313  |      -3.3663   |
| student_id_S3131 |       7.17355  |
| student_id_S3132 |       7.53351  |
| student_id_S3133 |       6.77803  |
| student_id_S3134 |      -6.11207  |
| student_id_S3135 |      -2.00294  |
| student_id_S3136 |      -8.18216  |
| student_id_S3137 |       0.999406 |
| student_id_S3138 |       2.11003  |

---

### Blocco 204 (Feature 2031 - 2040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3139 |        7.05663 |
| student_id_S3140 |        7.15589 |
| student_id_S3141 |       -8.89989 |
| student_id_S3142 |        1.956   |
| student_id_S3143 |        1.0244  |
| student_id_S3144 |      -15.5044  |
| student_id_S3145 |       -4.34981 |
| student_id_S3146 |        6.55893 |
| student_id_S3147 |      -11.2742  |
| student_id_S3148 |       -5.16313 |

---

### Blocco 205 (Feature 2041 - 2050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3149 |        4.99986 |
| student_id_S315  |       -4.21012 |
| student_id_S3150 |        1.18214 |
| student_id_S3151 |        6.9718  |
| student_id_S3152 |        4.32227 |
| student_id_S3153 |        3.14828 |
| student_id_S3154 |        2.12096 |
| student_id_S3155 |       11.3737  |
| student_id_S3156 |        5.22055 |
| student_id_S3157 |       -1.39745 |

---

### Blocco 206 (Feature 2051 - 2060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3158 |      12.3247   |
| student_id_S316  |      -7.12999  |
| student_id_S3160 |       4.84575  |
| student_id_S3161 |       8.81407  |
| student_id_S3162 |       7.24859  |
| student_id_S3163 |       0.366659 |
| student_id_S3164 |       5.01797  |
| student_id_S3166 |       6.7705   |
| student_id_S3167 |       7.57889  |
| student_id_S3168 |      12.9119   |

---

### Blocco 207 (Feature 2061 - 2070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3169 |      -6.08264  |
| student_id_S3170 |     -10.8694   |
| student_id_S3171 |     -10.4859   |
| student_id_S3172 |      -9.98109  |
| student_id_S3175 |       5.74966  |
| student_id_S3176 |       5.82959  |
| student_id_S3177 |      -0.822386 |
| student_id_S3178 |      -1.64844  |
| student_id_S318  |      -3.76096  |
| student_id_S3180 |       4.01842  |

---

### Blocco 208 (Feature 2071 - 2080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3181 |      -12.7667  |
| student_id_S3182 |        4.12553 |
| student_id_S3183 |        2.8534  |
| student_id_S3185 |       -8.4803  |
| student_id_S3186 |       -7.31247 |
| student_id_S3187 |        2.41853 |
| student_id_S3188 |       -2.05874 |
| student_id_S3189 |       11.0722  |
| student_id_S319  |       11.5033  |
| student_id_S3190 |       13.2188  |

---

### Blocco 209 (Feature 2081 - 2090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3191 |       10.1012  |
| student_id_S3192 |       12.6262  |
| student_id_S3193 |       -1.75115 |
| student_id_S3194 |       11.6559  |
| student_id_S3195 |        3.73525 |
| student_id_S3196 |       -9.63961 |
| student_id_S3197 |       -6.35112 |
| student_id_S3198 |        8.70748 |
| student_id_S3199 |       -8.07584 |
| student_id_S32   |       -1.51228 |

---

### Blocco 210 (Feature 2091 - 2100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S320  |      -2.43555  |
| student_id_S3200 |      -3.23538  |
| student_id_S3202 |      -9.2693   |
| student_id_S3203 |       9.61126  |
| student_id_S3204 |      10.3905   |
| student_id_S3205 |      -2.38489  |
| student_id_S3206 |      -8.28097  |
| student_id_S3207 |       4.75843  |
| student_id_S3209 |      -0.495027 |
| student_id_S321  |      -3.64832  |

---

### Blocco 211 (Feature 2101 - 2110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3210 |    -8.32766    |
| student_id_S3211 |    -1.68273    |
| student_id_S3212 |     0.00869362 |
| student_id_S3213 |     5.02481    |
| student_id_S3214 |    -6.68339    |
| student_id_S3215 |    -5.37613    |
| student_id_S3216 |    -4.2287     |
| student_id_S3217 |    -1.04986    |
| student_id_S3218 |     4.81674    |
| student_id_S3219 |     1.14438    |

---

### Blocco 212 (Feature 2111 - 2120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3220 |       5.327    |
| student_id_S3221 |       3.48528  |
| student_id_S3222 |      -5.33187  |
| student_id_S3223 |       8.85251  |
| student_id_S3224 |       8.66408  |
| student_id_S3225 |      11.793    |
| student_id_S3227 |      -1.78529  |
| student_id_S3229 |      -3.09957  |
| student_id_S323  |      -4.83983  |
| student_id_S3230 |      -0.429562 |

---

### Blocco 213 (Feature 2121 - 2130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3232 |       3.4754   |
| student_id_S3233 |      -6.25349  |
| student_id_S3234 |     -10.189    |
| student_id_S3235 |      -3.78763  |
| student_id_S3236 |       7.60238  |
| student_id_S3237 |      -6.88745  |
| student_id_S3238 |      -0.802366 |
| student_id_S324  |      -3.66887  |
| student_id_S3240 |       6.21637  |
| student_id_S3241 |      -0.934761 |

---

### Blocco 214 (Feature 2131 - 2140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3242 |       -8.80373 |
| student_id_S3243 |       -1.84788 |
| student_id_S3244 |       -2.76708 |
| student_id_S3248 |       11.2627  |
| student_id_S3249 |       10.2228  |
| student_id_S325  |        5.69035 |
| student_id_S3250 |      -13.7713  |
| student_id_S3251 |        4.47555 |
| student_id_S3252 |        1.8494  |
| student_id_S3253 |        1.03781 |

---

### Blocco 215 (Feature 2141 - 2150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3254 |       0.512356 |
| student_id_S3255 |       7.13841  |
| student_id_S3257 |       1.61118  |
| student_id_S3258 |      10.3947   |
| student_id_S3259 |      -1.66676  |
| student_id_S326  |      -7.3407   |
| student_id_S3261 |       5.65965  |
| student_id_S3262 |      -9.25034  |
| student_id_S3264 |      -6.41708  |
| student_id_S3266 |      -3.21717  |

---

### Blocco 216 (Feature 2151 - 2160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3267 |      -4.99806  |
| student_id_S3269 |       7.21678  |
| student_id_S3270 |      -2.53917  |
| student_id_S3271 |       9.13181  |
| student_id_S3272 |      -1.58986  |
| student_id_S3273 |      -4.50494  |
| student_id_S3274 |      14.0867   |
| student_id_S3275 |      -4.58095  |
| student_id_S3276 |      -1.88109  |
| student_id_S3277 |       0.763941 |

---

### Blocco 217 (Feature 2161 - 2170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3278 |      -5.31404  |
| student_id_S328  |      -6.8879   |
| student_id_S3280 |       0.910788 |
| student_id_S3281 |       7.10927  |
| student_id_S3282 |     -12.3531   |
| student_id_S3283 |      -2.77651  |
| student_id_S3284 |      10.2969   |
| student_id_S3285 |      -1.03777  |
| student_id_S3286 |       0.783144 |
| student_id_S3288 |       7.78234  |

---

### Blocco 218 (Feature 2171 - 2180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3289 |        4.90646 |
| student_id_S329  |        1.82495 |
| student_id_S3290 |       -6.24541 |
| student_id_S3291 |        5.324   |
| student_id_S3292 |      -11.5201  |
| student_id_S3293 |        1.2775  |
| student_id_S3294 |        9.08193 |
| student_id_S3295 |       -7.3475  |
| student_id_S3296 |        1.99087 |
| student_id_S3297 |        2.25992 |

---

### Blocco 219 (Feature 2181 - 2190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3298 |      -2.81159  |
| student_id_S3299 |      -5.33502  |
| student_id_S330  |      -2.86295  |
| student_id_S3300 |      -4.94434  |
| student_id_S3301 |       2.40898  |
| student_id_S3302 |       3.07532  |
| student_id_S3303 |       1.91337  |
| student_id_S3304 |      -3.16434  |
| student_id_S3305 |      -0.159681 |
| student_id_S3306 |       8.92323  |

---

### Blocco 220 (Feature 2191 - 2200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3307 |       1.10132  |
| student_id_S3309 |       0.193042 |
| student_id_S331  |      -0.622216 |
| student_id_S3310 |      13.2951   |
| student_id_S3311 |      -2.46104  |
| student_id_S3312 |      -1.71724  |
| student_id_S3313 |      14.1017   |
| student_id_S3314 |      17.7966   |
| student_id_S3315 |      -5.76903  |
| student_id_S3316 |      -1.91873  |

---

### Blocco 221 (Feature 2201 - 2210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3317 |       -7.32829 |
| student_id_S3318 |      -10.0231  |
| student_id_S3319 |        1.55527 |
| student_id_S332  |        1.23176 |
| student_id_S3320 |       -2.14206 |
| student_id_S3322 |        7.12081 |
| student_id_S3324 |        4.67798 |
| student_id_S3325 |        7.76839 |
| student_id_S3326 |        2.3748  |
| student_id_S3327 |       13.4938  |

---

### Blocco 222 (Feature 2211 - 2220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3328 |     11.9819    |
| student_id_S3329 |      5.74118   |
| student_id_S333  |      0.0258765 |
| student_id_S3330 |     -5.4649    |
| student_id_S3331 |     -6.38647   |
| student_id_S3332 |      2.46444   |
| student_id_S3333 |     10.7889    |
| student_id_S3336 |     -8.99042   |
| student_id_S3337 |      2.49386   |
| student_id_S3339 |      2.54644   |

---

### Blocco 223 (Feature 2221 - 2230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S334  |      -4.76805  |
| student_id_S3340 |       1.58339  |
| student_id_S3341 |      -8.62918  |
| student_id_S3342 |       1.97708  |
| student_id_S3343 |       3.35388  |
| student_id_S3344 |      -0.135696 |
| student_id_S3345 |       0.348566 |
| student_id_S3346 |       7.5955   |
| student_id_S3347 |       9.94053  |
| student_id_S3348 |      -3.48445  |

---

### Blocco 224 (Feature 2231 - 2240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S335  |      -0.780216 |
| student_id_S3350 |      -5.43259  |
| student_id_S3352 |       3.20537  |
| student_id_S3353 |     -13.8421   |
| student_id_S3354 |      -6.50628  |
| student_id_S3355 |      -2.0727   |
| student_id_S3356 |      -4.80256  |
| student_id_S3357 |      -8.17091  |
| student_id_S3358 |       8.63427  |
| student_id_S336  |       7.70666  |

---

### Blocco 225 (Feature 2241 - 2250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3360 |      -6.54336  |
| student_id_S3361 |      -8.7637   |
| student_id_S3362 |      -0.169584 |
| student_id_S3363 |     -10.2871   |
| student_id_S3364 |       2.13275  |
| student_id_S3365 |       5.58301  |
| student_id_S3366 |      -8.73631  |
| student_id_S3367 |       1.64786  |
| student_id_S3368 |      -0.48438  |
| student_id_S337  |      -0.829341 |

---

### Blocco 226 (Feature 2251 - 2260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3370 |      -8.64261  |
| student_id_S3371 |       7.36099  |
| student_id_S3373 |       2.12787  |
| student_id_S3374 |      -8.10819  |
| student_id_S3375 |       3.86461  |
| student_id_S3376 |      -1.51529  |
| student_id_S3377 |      11.5565   |
| student_id_S3378 |       0.296118 |
| student_id_S3379 |       6.11689  |
| student_id_S3380 |      10.8912   |

---

### Blocco 227 (Feature 2261 - 2270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3381 |       -2.58938 |
| student_id_S3382 |        7.68627 |
| student_id_S3383 |       -2.34104 |
| student_id_S3384 |       -2.96995 |
| student_id_S3385 |        7.48666 |
| student_id_S3386 |       -2.10841 |
| student_id_S3387 |      -11.7078  |
| student_id_S3388 |       12.7559  |
| student_id_S3389 |       13.6106  |
| student_id_S339  |       13.8795  |

---

### Blocco 228 (Feature 2271 - 2280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3390 |        8.91513 |
| student_id_S3391 |       -7.07945 |
| student_id_S3392 |       -4.86587 |
| student_id_S3393 |        7.01149 |
| student_id_S3394 |       -5.07561 |
| student_id_S3395 |       -2.98512 |
| student_id_S3396 |       -3.961   |
| student_id_S3397 |       -6.18503 |
| student_id_S3399 |       -3.81931 |
| student_id_S34   |        6.0239  |

---

### Blocco 229 (Feature 2281 - 2290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S340  |     -0.498478  |
| student_id_S3400 |      0.0404234 |
| student_id_S3401 |     -1.63074   |
| student_id_S3402 |      7.72092   |
| student_id_S3403 |      1.90125   |
| student_id_S3404 |     -1.91322   |
| student_id_S3405 |      5.07624   |
| student_id_S3406 |      0.730471  |
| student_id_S3407 |      3.94308   |
| student_id_S3408 |     12.5206    |

---

### Blocco 230 (Feature 2291 - 2300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3409 |     -1.00222   |
| student_id_S341  |     -3.92363   |
| student_id_S3410 |      9.30785   |
| student_id_S3411 |      7.93547   |
| student_id_S3412 |      2.76825   |
| student_id_S3413 |      0.601788  |
| student_id_S3414 |     -0.0984818 |
| student_id_S3416 |      6.17018   |
| student_id_S3418 |     -3.22564   |
| student_id_S3419 |     -9.10151   |

---

### Blocco 231 (Feature 2301 - 2310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S342  |      -11.995   |
| student_id_S3420 |        1.88909 |
| student_id_S3421 |        9.17336 |
| student_id_S3422 |       -3.56678 |
| student_id_S3423 |        1.97074 |
| student_id_S3424 |       -1.43461 |
| student_id_S3425 |       -5.30324 |
| student_id_S3426 |       -5.27463 |
| student_id_S3427 |        6.15847 |
| student_id_S3428 |       11.882   |

---

### Blocco 232 (Feature 2311 - 2320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3429 |       -4.62318 |
| student_id_S3430 |        4.58113 |
| student_id_S3431 |        2.19135 |
| student_id_S3432 |       -3.02232 |
| student_id_S3433 |       -8.60021 |
| student_id_S3434 |       -3.35574 |
| student_id_S3435 |      -11.7548  |
| student_id_S3436 |       -6.96985 |
| student_id_S3437 |       13.517   |
| student_id_S3438 |       -4.57725 |

---

### Blocco 233 (Feature 2321 - 2330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S344  |       3.2447   |
| student_id_S3440 |      -4.81485  |
| student_id_S3441 |       1.03002  |
| student_id_S3442 |      -9.4364   |
| student_id_S3443 |       5.08224  |
| student_id_S3444 |       3.04224  |
| student_id_S3446 |      -2.25924  |
| student_id_S3447 |       4.01537  |
| student_id_S3448 |       0.796612 |
| student_id_S3449 |       3.14208  |

---

### Blocco 234 (Feature 2331 - 2340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S345  |     -1.34836   |
| student_id_S3450 |     -1.27292   |
| student_id_S3451 |     -0.222085  |
| student_id_S3452 |     10.9399    |
| student_id_S3453 |      8.21663   |
| student_id_S3454 |     -0.0771169 |
| student_id_S3455 |      5.53031   |
| student_id_S3456 |      5.09656   |
| student_id_S3457 |     10.6787    |
| student_id_S3458 |     -0.810796  |

---

### Blocco 235 (Feature 2341 - 2350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3459 |      -0.332736 |
| student_id_S3461 |      11.5998   |
| student_id_S3462 |      -5.67736  |
| student_id_S3463 |      -6.80988  |
| student_id_S3465 |      -1.56503  |
| student_id_S3466 |       4.40541  |
| student_id_S3467 |      -4.97773  |
| student_id_S3468 |      -4.74555  |
| student_id_S347  |      11.6066   |
| student_id_S3470 |      10.0489   |

---

### Blocco 236 (Feature 2351 - 2360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3471 |       7.41503  |
| student_id_S3472 |      -6.89212  |
| student_id_S3473 |      14.9299   |
| student_id_S3474 |      -3.1895   |
| student_id_S3475 |       0.364337 |
| student_id_S3476 |      -3.79248  |
| student_id_S3477 |      -0.322426 |
| student_id_S3478 |       8.65574  |
| student_id_S348  |       7.07956  |
| student_id_S3481 |       4.16291  |

---

### Blocco 237 (Feature 2361 - 2370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3482 |      13.3695   |
| student_id_S3485 |      -2.78739  |
| student_id_S3486 |      -7.01401  |
| student_id_S3487 |      -4.58903  |
| student_id_S3489 |       2.44116  |
| student_id_S349  |      -9.94008  |
| student_id_S3490 |      -0.407616 |
| student_id_S3491 |       6.1252   |
| student_id_S3492 |      -0.306296 |
| student_id_S3493 |      -1.38393  |

---

### Blocco 238 (Feature 2371 - 2380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3495 |      14.9624   |
| student_id_S3496 |      -8.59337  |
| student_id_S3497 |       1.84639  |
| student_id_S3498 |      13.3953   |
| student_id_S3499 |      -0.589993 |
| student_id_S350  |       7.91233  |
| student_id_S3500 |       6.32279  |
| student_id_S3501 |       2.71793  |
| student_id_S3502 |      -8.4962   |
| student_id_S3503 |      -2.24476  |

---

### Blocco 239 (Feature 2381 - 2390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3504 |       13.8192  |
| student_id_S3507 |        5.85732 |
| student_id_S3508 |      -11.1299  |
| student_id_S3509 |        1.12465 |
| student_id_S351  |       16.2362  |
| student_id_S3510 |      -10.6202  |
| student_id_S3511 |       -8.83143 |
| student_id_S3512 |       -9.82204 |
| student_id_S3513 |       -7.84767 |
| student_id_S3514 |        3.18308 |

---

### Blocco 240 (Feature 2391 - 2400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3515 |      -3.55675  |
| student_id_S3516 |      -8.04886  |
| student_id_S3517 |       4.56005  |
| student_id_S3518 |      -7.14958  |
| student_id_S3519 |      12.5741   |
| student_id_S352  |      -2.15317  |
| student_id_S3520 |      -5.30535  |
| student_id_S3521 |      -0.332817 |
| student_id_S3522 |      -6.25999  |
| student_id_S3523 |      -0.472156 |

---

### Blocco 241 (Feature 2401 - 2410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3524 |      -3.13758  |
| student_id_S3526 |       0.593339 |
| student_id_S3527 |      12.9773   |
| student_id_S3528 |       0.971618 |
| student_id_S3529 |      -9.04205  |
| student_id_S353  |      -2.43641  |
| student_id_S3530 |      -8.64308  |
| student_id_S3531 |       1.82445  |
| student_id_S3532 |      15.4188   |
| student_id_S3533 |      -0.234933 |

---

### Blocco 242 (Feature 2411 - 2420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3534 |       -2.85714 |
| student_id_S3535 |        2.59491 |
| student_id_S3536 |       -7.35374 |
| student_id_S3537 |        3.96785 |
| student_id_S3538 |        3.43001 |
| student_id_S3539 |        2.29596 |
| student_id_S3540 |       -3.48645 |
| student_id_S3542 |        7.06087 |
| student_id_S3543 |       -9.57522 |
| student_id_S3544 |       -1.29453 |

---

### Blocco 243 (Feature 2421 - 2430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3545 |       -1.34887 |
| student_id_S3546 |        1.49676 |
| student_id_S3547 |        2.48729 |
| student_id_S3548 |        6.78975 |
| student_id_S3549 |      -12.3824  |
| student_id_S355  |       11.5438  |
| student_id_S3551 |        2.37298 |
| student_id_S3552 |        2.17851 |
| student_id_S3553 |       19.3224  |
| student_id_S3555 |       14.2989  |

---

### Blocco 244 (Feature 2431 - 2440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3556 |      -7.37717  |
| student_id_S3557 |      -4.69913  |
| student_id_S3558 |       1.98239  |
| student_id_S3559 |     -12.5576   |
| student_id_S356  |      -0.485265 |
| student_id_S3560 |      15.0421   |
| student_id_S3561 |       3.99016  |
| student_id_S3562 |      -6.17633  |
| student_id_S3563 |       4.92744  |
| student_id_S3564 |      -3.47478  |

---

### Blocco 245 (Feature 2441 - 2450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3565 |       5.53656  |
| student_id_S3566 |       4.59805  |
| student_id_S3567 |       5.44772  |
| student_id_S3568 |       3.66127  |
| student_id_S3569 |       8.86963  |
| student_id_S357  |       0.932666 |
| student_id_S3571 |      14.208    |
| student_id_S3572 |       1.09271  |
| student_id_S3573 |       7.0205   |
| student_id_S3574 |      -6.24289  |

---

### Blocco 246 (Feature 2451 - 2460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3575 |      -8.0295   |
| student_id_S3576 |      -1.47848  |
| student_id_S3577 |       3.39538  |
| student_id_S3579 |      -4.02264  |
| student_id_S358  |      -7.77207  |
| student_id_S3580 |      -4.92364  |
| student_id_S3581 |      12.8913   |
| student_id_S3582 |      -2.86176  |
| student_id_S3583 |      -8.92428  |
| student_id_S3585 |       0.668164 |

---

### Blocco 247 (Feature 2461 - 2470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3587 |        1.53045 |
| student_id_S3588 |        5.8192  |
| student_id_S3589 |       -4.37062 |
| student_id_S3590 |        5.78494 |
| student_id_S3591 |       -4.35833 |
| student_id_S3593 |        2.20087 |
| student_id_S3594 |       -4.31781 |
| student_id_S3596 |        9.72152 |
| student_id_S3597 |        9.28898 |
| student_id_S3598 |        8.70939 |

---

### Blocco 248 (Feature 2471 - 2480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3599 |        9.23854 |
| student_id_S36   |       -2.88776 |
| student_id_S360  |       16.3414  |
| student_id_S3601 |        5.01992 |
| student_id_S3603 |       -7.28494 |
| student_id_S3604 |        9.7909  |
| student_id_S3605 |       12.6811  |
| student_id_S3608 |        6.4717  |
| student_id_S3609 |       -4.34048 |
| student_id_S361  |       -6.49649 |

---

### Blocco 249 (Feature 2481 - 2490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3610 |        2.25417 |
| student_id_S3611 |        2.26559 |
| student_id_S3613 |        4.25308 |
| student_id_S3614 |       10.4902  |
| student_id_S3615 |       -2.2595  |
| student_id_S3616 |        4.46769 |
| student_id_S3617 |        2.42959 |
| student_id_S3618 |        8.63708 |
| student_id_S3619 |       -2.82502 |
| student_id_S362  |       -4.60818 |

---

### Blocco 250 (Feature 2491 - 2500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3620 |       4.04616  |
| student_id_S3621 |      -3.242    |
| student_id_S3622 |       9.98589  |
| student_id_S3623 |       3.93082  |
| student_id_S3624 |      -5.08372  |
| student_id_S3625 |      -1.99714  |
| student_id_S3626 |      11.3602   |
| student_id_S3627 |       0.280038 |
| student_id_S3629 |     -10.7383   |
| student_id_S363  |     -10.3584   |

---

### Blocco 251 (Feature 2501 - 2510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3630 |     -0.321097  |
| student_id_S3631 |     11.9897    |
| student_id_S3632 |     -1.88901   |
| student_id_S3633 |     -4.16906   |
| student_id_S3635 |      9.66387   |
| student_id_S3636 |      0.0519477 |
| student_id_S3637 |     14.1573    |
| student_id_S3638 |     -6.08405   |
| student_id_S3639 |      4.02596   |
| student_id_S364  |      8.90045   |

---

### Blocco 252 (Feature 2511 - 2520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3640 |      -1.83147  |
| student_id_S3641 |      -2.87816  |
| student_id_S3642 |      15.2258   |
| student_id_S3643 |       0.740327 |
| student_id_S3644 |     -13.6964   |
| student_id_S3645 |      -0.434488 |
| student_id_S3646 |       6.16614  |
| student_id_S3647 |       0.801917 |
| student_id_S3649 |     -10.6225   |
| student_id_S365  |      -4.49439  |

---

### Blocco 253 (Feature 2521 - 2530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3650 |        4.61323 |
| student_id_S3651 |        9.53377 |
| student_id_S3652 |       -1.3376  |
| student_id_S3653 |        4.26745 |
| student_id_S3654 |       -7.38653 |
| student_id_S3655 |       -5.63101 |
| student_id_S3657 |        7.69769 |
| student_id_S3658 |       -5.5856  |
| student_id_S3659 |        6.34144 |
| student_id_S366  |       -6.99393 |

---

### Blocco 254 (Feature 2531 - 2540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3660 |      -1.91505  |
| student_id_S3662 |      -0.782485 |
| student_id_S3663 |       7.96782  |
| student_id_S3664 |      -0.530531 |
| student_id_S3665 |      -2.11962  |
| student_id_S3666 |      11.6146   |
| student_id_S3667 |       1.06979  |
| student_id_S3668 |       3.28415  |
| student_id_S3669 |       7.02749  |
| student_id_S367  |      -2.28819  |

---

### Blocco 255 (Feature 2541 - 2550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3671 |       -1.66681 |
| student_id_S3672 |       -7.23402 |
| student_id_S3673 |        1.98936 |
| student_id_S3674 |       11.4119  |
| student_id_S3675 |        8.30739 |
| student_id_S3676 |        6.96783 |
| student_id_S3677 |       15.759   |
| student_id_S3678 |        3.82984 |
| student_id_S3679 |        8.58322 |
| student_id_S368  |       12.1611  |

---

### Blocco 256 (Feature 2551 - 2560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3680 |      -4.7436   |
| student_id_S3681 |      -1.67591  |
| student_id_S3682 |      -5.24005  |
| student_id_S3683 |      -2.78454  |
| student_id_S3684 |       0.992961 |
| student_id_S3685 |       5.40394  |
| student_id_S3687 |      -3.18386  |
| student_id_S3688 |       2.7407   |
| student_id_S3689 |      -2.521    |
| student_id_S369  |      -7.66258  |

---

### Blocco 257 (Feature 2561 - 2570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3690 |       -8.46851 |
| student_id_S3691 |        8.93784 |
| student_id_S3693 |        6.07045 |
| student_id_S3694 |       12.6717  |
| student_id_S3695 |        3.11266 |
| student_id_S3696 |      -13.6326  |
| student_id_S3697 |       -2.83128 |
| student_id_S3698 |       -3.36523 |
| student_id_S3699 |       -5.77084 |
| student_id_S37   |       10.9926  |

---

### Blocco 258 (Feature 2571 - 2580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3700 |     -14.5578   |
| student_id_S3701 |       0.460442 |
| student_id_S3702 |     -12.6886   |
| student_id_S3705 |      -1.8887   |
| student_id_S3706 |       2.90606  |
| student_id_S3707 |      -7.65877  |
| student_id_S3708 |       2.06187  |
| student_id_S3709 |      -9.0239   |
| student_id_S371  |      -0.529665 |
| student_id_S3710 |      -3.60213  |

---

### Blocco 259 (Feature 2581 - 2590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3711 |       3.892    |
| student_id_S3713 |      -6.43401  |
| student_id_S3714 |       8.91112  |
| student_id_S3715 |      -2.42268  |
| student_id_S3716 |      -0.942689 |
| student_id_S3717 |     -12.2949   |
| student_id_S3719 |      -0.945551 |
| student_id_S372  |       8.74597  |
| student_id_S3720 |      -5.12898  |
| student_id_S3721 |      -5.97477  |

---

### Blocco 260 (Feature 2591 - 2600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3722 |        2.30335 |
| student_id_S3723 |        2.40609 |
| student_id_S3725 |       12.9098  |
| student_id_S3726 |        4.22434 |
| student_id_S3727 |       -9.04925 |
| student_id_S3728 |       13.6119  |
| student_id_S3729 |       -8.70934 |
| student_id_S373  |       10.7755  |
| student_id_S3730 |        5.01437 |
| student_id_S3731 |       -3.44452 |

---

### Blocco 261 (Feature 2601 - 2610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3733 |       -3.37798 |
| student_id_S3734 |        1.81875 |
| student_id_S3735 |       -6.13596 |
| student_id_S3736 |       -5.95263 |
| student_id_S3737 |       -9.90697 |
| student_id_S3738 |        1.05856 |
| student_id_S3739 |        3.58682 |
| student_id_S374  |       -4.12721 |
| student_id_S3740 |       -1.6216  |
| student_id_S3742 |        8.39864 |

---

### Blocco 262 (Feature 2611 - 2620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3743 |       -6.66207 |
| student_id_S3744 |      -11.1315  |
| student_id_S3745 |        5.7984  |
| student_id_S3747 |       -1.23977 |
| student_id_S3749 |       19.1841  |
| student_id_S375  |       -7.30198 |
| student_id_S3750 |        9.75637 |
| student_id_S3751 |        8.33042 |
| student_id_S3752 |       -2.89488 |
| student_id_S3753 |       -5.5764  |

---

### Blocco 263 (Feature 2621 - 2630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3756 |      -3.84794  |
| student_id_S3757 |      -6.88378  |
| student_id_S3758 |       9.03497  |
| student_id_S3759 |      -0.955287 |
| student_id_S376  |       0.284929 |
| student_id_S3760 |     -10.6184   |
| student_id_S3763 |       5.19099  |
| student_id_S3764 |      -0.552816 |
| student_id_S3765 |       0.996504 |
| student_id_S3766 |      -7.30525  |

---

### Blocco 264 (Feature 2631 - 2640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3767 |       3.6002   |
| student_id_S3768 |      17.0101   |
| student_id_S3769 |       0.527523 |
| student_id_S377  |       7.81588  |
| student_id_S3770 |      -9.84074  |
| student_id_S3771 |       0.611913 |
| student_id_S3772 |       6.79858  |
| student_id_S3773 |      -1.17817  |
| student_id_S3774 |      -7.502    |
| student_id_S3776 |       1.58488  |

---

### Blocco 265 (Feature 2641 - 2650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3777 |      -8.15635  |
| student_id_S3778 |       5.41113  |
| student_id_S3779 |      -5.29717  |
| student_id_S378  |      -6.17975  |
| student_id_S3780 |      -9.97858  |
| student_id_S3782 |      -3.57406  |
| student_id_S3783 |      -0.209653 |
| student_id_S3785 |      11.2301   |
| student_id_S3786 |       1.99139  |
| student_id_S3787 |       4.54101  |

---

### Blocco 266 (Feature 2651 - 2660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3788 |      -0.021035 |
| student_id_S3789 |       4.22649  |
| student_id_S379  |      -5.83938  |
| student_id_S3790 |     -13.9279   |
| student_id_S3792 |       3.08925  |
| student_id_S3793 |       3.15115  |
| student_id_S3794 |       4.68286  |
| student_id_S3796 |       8.28202  |
| student_id_S3797 |       3.0681   |
| student_id_S3798 |      -4.69669  |

---

### Blocco 267 (Feature 2661 - 2670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S38   |     -10.2503   |
| student_id_S3800 |      -0.202179 |
| student_id_S3801 |      -6.88041  |
| student_id_S3802 |       7.4979   |
| student_id_S3803 |     -10.0043   |
| student_id_S3804 |       6.0047   |
| student_id_S3805 |       6.57191  |
| student_id_S3806 |      -3.81976  |
| student_id_S3807 |      -0.428568 |
| student_id_S3808 |       5.39594  |

---

### Blocco 268 (Feature 2671 - 2680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3809 |     -3.20381   |
| student_id_S381  |      8.54513   |
| student_id_S3810 |     -0.799615  |
| student_id_S3812 |      1.3253    |
| student_id_S3813 |      6.87445   |
| student_id_S3814 |      4.04157   |
| student_id_S3815 |     -0.0429007 |
| student_id_S3816 |     -4.08946   |
| student_id_S3818 |     -4.22171   |
| student_id_S382  |     -6.8979    |

---

### Blocco 269 (Feature 2681 - 2690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3820 |      9.94769   |
| student_id_S3821 |     -6.31295   |
| student_id_S3823 |      4.74941   |
| student_id_S3824 |     11.1456    |
| student_id_S3825 |      0.0769073 |
| student_id_S3826 |     13.7096    |
| student_id_S3827 |    -14.5408    |
| student_id_S3828 |     -8.25769   |
| student_id_S3829 |     -4.02463   |
| student_id_S3830 |      7.32227   |

---

### Blocco 270 (Feature 2691 - 2700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3832 |        3.08632 |
| student_id_S3833 |       15.8037  |
| student_id_S3834 |       -1.20907 |
| student_id_S3835 |        7.21732 |
| student_id_S3836 |       -6.15053 |
| student_id_S3837 |       -1.36171 |
| student_id_S3838 |        7.86674 |
| student_id_S3839 |       -3.58807 |
| student_id_S384  |        8.55542 |
| student_id_S3840 |        2.20909 |

---

### Blocco 271 (Feature 2701 - 2710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3842 |       9.5741   |
| student_id_S3843 |       4.22956  |
| student_id_S3844 |      14.947    |
| student_id_S3845 |      -0.101995 |
| student_id_S3846 |      -2.03101  |
| student_id_S3848 |     -11.2789   |
| student_id_S385  |      -6.63177  |
| student_id_S3850 |       8.74998  |
| student_id_S3852 |       6.2333   |
| student_id_S3853 |      -0.75759  |

---

### Blocco 272 (Feature 2711 - 2720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3855 |       12.3632  |
| student_id_S3857 |        3.13641 |
| student_id_S3858 |       -5.44045 |
| student_id_S3859 |       11.5676  |
| student_id_S386  |       -4.76924 |
| student_id_S3860 |      -12.872   |
| student_id_S3861 |       -4.13481 |
| student_id_S3862 |        2.37764 |
| student_id_S3864 |       -5.72802 |
| student_id_S3865 |       -2.09426 |

---

### Blocco 273 (Feature 2721 - 2730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3866 |       1.22496  |
| student_id_S3867 |       0.160759 |
| student_id_S3868 |      -1.19852  |
| student_id_S3869 |      10.8886   |
| student_id_S387  |       9.44405  |
| student_id_S3870 |       5.14222  |
| student_id_S3871 |       7.68316  |
| student_id_S3872 |       8.42473  |
| student_id_S3873 |       9.83327  |
| student_id_S3874 |      -0.624342 |

---

### Blocco 274 (Feature 2731 - 2740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3875 |       0.810336 |
| student_id_S3876 |       6.03534  |
| student_id_S3877 |      -7.13049  |
| student_id_S3878 |       3.90687  |
| student_id_S3879 |      -8.73796  |
| student_id_S388  |       0.964362 |
| student_id_S3880 |      -1.47997  |
| student_id_S3881 |      -1.34277  |
| student_id_S3882 |      10.1611   |
| student_id_S3883 |      -2.92696  |

---

### Blocco 275 (Feature 2741 - 2750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3886 |       -7.44245 |
| student_id_S3887 |       -3.30774 |
| student_id_S3888 |       -3.98826 |
| student_id_S3889 |        7.00706 |
| student_id_S389  |        2.46954 |
| student_id_S3890 |       -9.37575 |
| student_id_S3891 |       -1.85267 |
| student_id_S3892 |       -9.10052 |
| student_id_S3893 |       11.2458  |
| student_id_S3894 |       -1.25308 |

---

### Blocco 276 (Feature 2751 - 2760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3895 |       5.25526  |
| student_id_S3896 |       2.39891  |
| student_id_S3897 |       6.53631  |
| student_id_S3898 |      -9.30441  |
| student_id_S3899 |       9.63853  |
| student_id_S39   |       0.41795  |
| student_id_S390  |       1.24296  |
| student_id_S3900 |      -8.27533  |
| student_id_S3901 |       0.852471 |
| student_id_S3902 |      -6.16218  |

---

### Blocco 277 (Feature 2761 - 2770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3903 |      -4.53514  |
| student_id_S3904 |       1.50885  |
| student_id_S3905 |      -8.73898  |
| student_id_S3906 |      -6.55254  |
| student_id_S3907 |      -7.51904  |
| student_id_S3908 |     -13.0774   |
| student_id_S3909 |      -0.243725 |
| student_id_S391  |       6.66459  |
| student_id_S3910 |       1.42492  |
| student_id_S3911 |      -3.51651  |

---

### Blocco 278 (Feature 2771 - 2780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3912 |      -2.41627  |
| student_id_S3913 |       0.467137 |
| student_id_S3914 |      -8.71005  |
| student_id_S3915 |      14.1116   |
| student_id_S3916 |      14.9667   |
| student_id_S3917 |      13.7264   |
| student_id_S3918 |       9.88936  |
| student_id_S3920 |       0.764951 |
| student_id_S3921 |     -15.3299   |
| student_id_S3923 |      -9.56154  |

---

### Blocco 279 (Feature 2781 - 2790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3924 |      14.6135   |
| student_id_S3925 |      -9.98709  |
| student_id_S3926 |       7.31343  |
| student_id_S3927 |      -5.49154  |
| student_id_S3928 |       2.22394  |
| student_id_S3929 |       2.90434  |
| student_id_S393  |       0.693135 |
| student_id_S3930 |       3.15667  |
| student_id_S3931 |      -1.56867  |
| student_id_S3932 |      -6.03106  |

---

### Blocco 280 (Feature 2791 - 2800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3934 |       -7.61623 |
| student_id_S3935 |        2.85903 |
| student_id_S3936 |       -5.01745 |
| student_id_S3937 |       12.7319  |
| student_id_S3939 |      -10.8305  |
| student_id_S394  |       -4.40047 |
| student_id_S3940 |       16.0742  |
| student_id_S3942 |       11.4708  |
| student_id_S3943 |      -12.3198  |
| student_id_S3944 |        7.86078 |

---

### Blocco 281 (Feature 2801 - 2810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3945 |      -4.07388  |
| student_id_S3946 |      -3.74917  |
| student_id_S3947 |     -13.7291   |
| student_id_S3948 |      -6.55061  |
| student_id_S3949 |       8.77775  |
| student_id_S395  |      14.6199   |
| student_id_S3950 |      -0.290613 |
| student_id_S3951 |       1.92603  |
| student_id_S3952 |     -10.3459   |
| student_id_S3953 |       6.96771  |

---

### Blocco 282 (Feature 2811 - 2820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3954 |       0.787874 |
| student_id_S3955 |       8.50335  |
| student_id_S3956 |       0.553713 |
| student_id_S3957 |      -4.27126  |
| student_id_S3958 |      -5.41875  |
| student_id_S396  |      10.1433   |
| student_id_S3960 |       0.399382 |
| student_id_S3961 |       4.28857  |
| student_id_S3962 |      -3.98511  |
| student_id_S3963 |      -3.14763  |

---

### Blocco 283 (Feature 2821 - 2830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3964 |      -0.484785 |
| student_id_S3965 |      -4.4416   |
| student_id_S3966 |       0.821989 |
| student_id_S3968 |      -6.30701  |
| student_id_S3969 |      -5.5336   |
| student_id_S397  |      -4.82869  |
| student_id_S3970 |       4.26557  |
| student_id_S3972 |      -9.95386  |
| student_id_S3973 |       1.2282   |
| student_id_S3975 |       7.128    |

---

### Blocco 284 (Feature 2831 - 2840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3976 |       2.09499  |
| student_id_S3977 |      -3.6634   |
| student_id_S3978 |      -4.89539  |
| student_id_S3979 |       0.928774 |
| student_id_S3980 |      -2.16791  |
| student_id_S3981 |       4.93082  |
| student_id_S3982 |      -3.02427  |
| student_id_S3984 |      -1.64769  |
| student_id_S3985 |       5.95392  |
| student_id_S3986 |      -2.28712  |

---

### Blocco 285 (Feature 2841 - 2850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S3987 |       6.9482   |
| student_id_S3988 |     -10.9826   |
| student_id_S3989 |      -3.6744   |
| student_id_S3990 |       4.57357  |
| student_id_S3993 |       2.49275  |
| student_id_S3994 |      -2.83805  |
| student_id_S3996 |      -3.79864  |
| student_id_S3997 |      -0.717723 |
| student_id_S3998 |      13.613    |
| student_id_S3999 |       1.74693  |

---

### Blocco 286 (Feature 2851 - 2860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4    |       11.7311  |
| student_id_S40   |        1.37137 |
| student_id_S400  |       19.822   |
| student_id_S4000 |        3.05014 |
| student_id_S4001 |       15.7492  |
| student_id_S4003 |        9.48523 |
| student_id_S4004 |       -5.34885 |
| student_id_S4005 |        6.31293 |
| student_id_S4006 |        5.74145 |
| student_id_S4007 |        8.37156 |

---

### Blocco 287 (Feature 2861 - 2870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4008 |       8.8197   |
| student_id_S4009 |      -8.86791  |
| student_id_S401  |       1.3498   |
| student_id_S4010 |       8.91088  |
| student_id_S4011 |       0.718032 |
| student_id_S4014 |      -7.08209  |
| student_id_S4015 |      15.0268   |
| student_id_S4016 |      -0.998545 |
| student_id_S4017 |       2.77884  |
| student_id_S4018 |       5.17773  |

---

### Blocco 288 (Feature 2871 - 2880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4019 |       -0.7456  |
| student_id_S402  |        5.97356 |
| student_id_S4020 |        4.35211 |
| student_id_S4022 |       -4.2282  |
| student_id_S4023 |        2.19043 |
| student_id_S4024 |       -5.96723 |
| student_id_S4025 |       -0.69772 |
| student_id_S4026 |       -1.60859 |
| student_id_S4027 |       -2.67726 |
| student_id_S4028 |        3.12613 |

---

### Blocco 289 (Feature 2881 - 2890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4029 |        3.24526 |
| student_id_S403  |      -10.1135  |
| student_id_S4030 |       -7.70153 |
| student_id_S4031 |       -6.48033 |
| student_id_S4032 |        8.35071 |
| student_id_S4033 |      -12.464   |
| student_id_S4034 |      -11.0301  |
| student_id_S4036 |       -4.28445 |
| student_id_S4037 |       -7.04467 |
| student_id_S4038 |        1.0467  |

---

### Blocco 290 (Feature 2891 - 2900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4039 |       12.2193  |
| student_id_S404  |       -1.75688 |
| student_id_S4040 |        3.03274 |
| student_id_S4041 |        6.85983 |
| student_id_S4042 |        7.63478 |
| student_id_S4044 |       -3.41366 |
| student_id_S4046 |       -8.5704  |
| student_id_S4047 |      -13.3465  |
| student_id_S4048 |       -6.16238 |
| student_id_S4049 |        1.72452 |

---

### Blocco 291 (Feature 2901 - 2910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S405  |      12.9626   |
| student_id_S4050 |      -0.800391 |
| student_id_S4052 |      -2.72851  |
| student_id_S4053 |       7.6331   |
| student_id_S4054 |       2.34084  |
| student_id_S4055 |       7.76286  |
| student_id_S4056 |      -1.25675  |
| student_id_S4057 |       4.41659  |
| student_id_S4058 |      -6.3927   |
| student_id_S4059 |      -8.74838  |

---

### Blocco 292 (Feature 2911 - 2920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S406  |      -6.64747  |
| student_id_S4060 |      -5.34172  |
| student_id_S4061 |       6.07798  |
| student_id_S4062 |       2.58724  |
| student_id_S4063 |     -11.1372   |
| student_id_S4065 |      11.6762   |
| student_id_S4066 |      -5.78235  |
| student_id_S4067 |       1.79536  |
| student_id_S4068 |       4.16412  |
| student_id_S4069 |       0.885011 |

---

### Blocco 293 (Feature 2921 - 2930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S407  |        2.24603 |
| student_id_S4070 |        8.34117 |
| student_id_S4072 |       -1.23525 |
| student_id_S4074 |       -4.22016 |
| student_id_S4075 |        6.89508 |
| student_id_S4077 |       -4.18662 |
| student_id_S4078 |       13.3545  |
| student_id_S4079 |       -5.39549 |
| student_id_S408  |       -6.17691 |
| student_id_S4080 |        6.23395 |

---

### Blocco 294 (Feature 2931 - 2940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4081 |      -2.01651  |
| student_id_S4082 |      -6.61864  |
| student_id_S4083 |       7.94551  |
| student_id_S4084 |      -2.33789  |
| student_id_S4085 |      12.8805   |
| student_id_S4086 |      -7.48568  |
| student_id_S4087 |      -6.93073  |
| student_id_S4089 |       6.86148  |
| student_id_S409  |       3.51735  |
| student_id_S4090 |      -0.083125 |

---

### Blocco 295 (Feature 2941 - 2950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4091 |       10.3639  |
| student_id_S4092 |       -2.61624 |
| student_id_S4093 |        7.98902 |
| student_id_S4094 |        7.74625 |
| student_id_S4097 |      -11.214   |
| student_id_S4098 |       -2.30585 |
| student_id_S41   |        9.28797 |
| student_id_S410  |        4.21671 |
| student_id_S4100 |       -6.32444 |
| student_id_S4101 |       -4.59567 |

---

### Blocco 296 (Feature 2951 - 2960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4102 |        4.95063 |
| student_id_S4103 |       -3.20755 |
| student_id_S4105 |       -1.25789 |
| student_id_S4108 |       -7.22664 |
| student_id_S4109 |       -6.8953  |
| student_id_S411  |        2.11404 |
| student_id_S4110 |        3.74254 |
| student_id_S4111 |        6.45194 |
| student_id_S4112 |        7.14474 |
| student_id_S4114 |      -14.7766  |

---

### Blocco 297 (Feature 2961 - 2970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4116 |      -7.07108  |
| student_id_S4117 |      -5.62775  |
| student_id_S4118 |      10.8278   |
| student_id_S412  |      -2.9842   |
| student_id_S4120 |       0.753876 |
| student_id_S4121 |       2.54293  |
| student_id_S4122 |       0.208157 |
| student_id_S4123 |       4.73004  |
| student_id_S4125 |      -6.2624   |
| student_id_S4126 |      -1.482    |

---

### Blocco 298 (Feature 2971 - 2980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4127 |      -6.75725  |
| student_id_S4128 |      -4.35772  |
| student_id_S4129 |      -5.43118  |
| student_id_S413  |      -3.42567  |
| student_id_S4130 |      -1.02055  |
| student_id_S4131 |      -0.700759 |
| student_id_S4133 |       1.3087   |
| student_id_S4134 |       7.812    |
| student_id_S4135 |      -7.64259  |
| student_id_S4136 |      -3.8856   |

---

### Blocco 299 (Feature 2981 - 2990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4137 |        2.22185 |
| student_id_S4138 |       -7.01387 |
| student_id_S4139 |      -11.9065  |
| student_id_S4140 |        5.41046 |
| student_id_S4141 |        8.21632 |
| student_id_S4142 |        2.21869 |
| student_id_S4143 |        5.801   |
| student_id_S4144 |        3.96822 |
| student_id_S4145 |       -0.4041  |
| student_id_S4146 |        2.29714 |

---

### Blocco 300 (Feature 2991 - 3000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4147 |       6.36683  |
| student_id_S4148 |      -1.4715   |
| student_id_S4149 |       7.69389  |
| student_id_S4150 |       6.08536  |
| student_id_S4151 |       5.68137  |
| student_id_S4153 |       0.440471 |
| student_id_S4154 |      -2.71708  |
| student_id_S4156 |       5.40977  |
| student_id_S4157 |      -3.22735  |
| student_id_S4158 |      -4.38781  |

---

### Blocco 301 (Feature 3001 - 3010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S416  |      -0.658488 |
| student_id_S4160 |       4.63393  |
| student_id_S4161 |       0.304992 |
| student_id_S4162 |       5.93483  |
| student_id_S4163 |       3.54108  |
| student_id_S4164 |       7.37706  |
| student_id_S4165 |       4.08665  |
| student_id_S4166 |      13.6486   |
| student_id_S4167 |       5.14423  |
| student_id_S4168 |       6.69882  |

---

### Blocco 302 (Feature 3011 - 3020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4169 |      2.47164   |
| student_id_S417  |     -7.616     |
| student_id_S4170 |      0.707218  |
| student_id_S4172 |      0.0801931 |
| student_id_S4173 |     -0.702946  |
| student_id_S4174 |     11.6476    |
| student_id_S4175 |    -18.038     |
| student_id_S4176 |      7.05589   |
| student_id_S4177 |      5.54726   |
| student_id_S4178 |      1.02764   |

---

### Blocco 303 (Feature 3021 - 3030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4179 |        2.60589 |
| student_id_S418  |      -11.8927  |
| student_id_S4180 |       -3.59556 |
| student_id_S4181 |        1.447   |
| student_id_S4182 |       -3.39579 |
| student_id_S4183 |       12.0321  |
| student_id_S4184 |      -12.1413  |
| student_id_S4185 |        2.693   |
| student_id_S4187 |       -3.95791 |
| student_id_S4190 |       -6.40554 |

---

### Blocco 304 (Feature 3031 - 3040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4191 |      -1.78609  |
| student_id_S4192 |       2.26451  |
| student_id_S4193 |       0.469934 |
| student_id_S4195 |       6.79909  |
| student_id_S4196 |       0.34216  |
| student_id_S4198 |      12.7004   |
| student_id_S4199 |      -5.01564  |
| student_id_S42   |     -10.4315   |
| student_id_S420  |      -3.23343  |
| student_id_S4200 |     -11.9933   |

---

### Blocco 305 (Feature 3041 - 3050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4203 |     -6.83144   |
| student_id_S4204 |      0.0514099 |
| student_id_S4205 |     -0.372486  |
| student_id_S4206 |     13.5858    |
| student_id_S4207 |    -19.2827    |
| student_id_S4208 |     -1.96947   |
| student_id_S4209 |     -3.18469   |
| student_id_S421  |      9.15161   |
| student_id_S4212 |      6.36666   |
| student_id_S4213 |     13.9651    |

---

### Blocco 306 (Feature 3051 - 3060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4216 |      -3.32758  |
| student_id_S4217 |       4.72576  |
| student_id_S4218 |       9.09295  |
| student_id_S4219 |      10.291    |
| student_id_S422  |       6.35553  |
| student_id_S4221 |       0.885686 |
| student_id_S4222 |       3.39189  |
| student_id_S4223 |      -7.51304  |
| student_id_S4224 |      12.8158   |
| student_id_S4225 |      -6.59832  |

---

### Blocco 307 (Feature 3061 - 3070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4226 |       9.78291  |
| student_id_S4227 |       9.7762   |
| student_id_S4228 |       8.35584  |
| student_id_S4229 |      -5.26189  |
| student_id_S423  |       0.951378 |
| student_id_S4230 |       9.42474  |
| student_id_S4231 |      -0.327276 |
| student_id_S4232 |      -1.75761  |
| student_id_S4233 |       1.70419  |
| student_id_S4234 |       1.23999  |

---

### Blocco 308 (Feature 3071 - 3080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4235 |      3.08473   |
| student_id_S4236 |      3.3738    |
| student_id_S4237 |     -0.0438583 |
| student_id_S4239 |     10.9999    |
| student_id_S424  |     -8.69275   |
| student_id_S4240 |     14.7499    |
| student_id_S4241 |     -9.71243   |
| student_id_S4242 |      5.84513   |
| student_id_S4243 |      1.68187   |
| student_id_S4244 |     -0.723238  |

---

### Blocco 309 (Feature 3081 - 3090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4246 |      -0.245878 |
| student_id_S4247 |     -10.3972   |
| student_id_S4249 |      -6.98083  |
| student_id_S425  |      -2.87157  |
| student_id_S4251 |       2.12169  |
| student_id_S4253 |      -4.96123  |
| student_id_S4254 |      -9.5466   |
| student_id_S4255 |      -6.79662  |
| student_id_S4256 |       7.91204  |
| student_id_S4257 |       3.8412   |

---

### Blocco 310 (Feature 3091 - 3100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4258 |      -6.17852  |
| student_id_S4259 |       8.16601  |
| student_id_S426  |       2.61292  |
| student_id_S4261 |       6.28678  |
| student_id_S4262 |      -4.46879  |
| student_id_S4263 |       7.12705  |
| student_id_S4265 |       3.35865  |
| student_id_S4266 |       0.578165 |
| student_id_S4267 |      -3.71107  |
| student_id_S4268 |       9.10667  |

---

### Blocco 311 (Feature 3101 - 3110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4269 |       6.82669  |
| student_id_S427  |       0.683046 |
| student_id_S4270 |      -4.78121  |
| student_id_S4271 |     -10.0001   |
| student_id_S4272 |       6.54534  |
| student_id_S4273 |       2.42042  |
| student_id_S4274 |      16.0518   |
| student_id_S4275 |      -8.53554  |
| student_id_S4276 |      -4.9682   |
| student_id_S4278 |      10.7328   |

---

### Blocco 312 (Feature 3111 - 3120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S428  |        6.1315  |
| student_id_S4280 |       -5.60522 |
| student_id_S4282 |       -4.00098 |
| student_id_S4283 |        0.24134 |
| student_id_S4284 |        8.48149 |
| student_id_S4285 |        2.0215  |
| student_id_S4286 |       -5.00874 |
| student_id_S4287 |        5.60115 |
| student_id_S4288 |        5.20731 |
| student_id_S4289 |        1.83287 |

---

### Blocco 313 (Feature 3121 - 3130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S429  |       2.35542  |
| student_id_S4290 |     -12.6741   |
| student_id_S4291 |     -10.4073   |
| student_id_S4292 |      -5.0316   |
| student_id_S4293 |      -5.96277  |
| student_id_S4294 |     -13.1733   |
| student_id_S4296 |       4.89391  |
| student_id_S4298 |       9.20164  |
| student_id_S4299 |      -0.733985 |
| student_id_S43   |      -3.43056  |

---

### Blocco 314 (Feature 3131 - 3140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S430  |        6.84038 |
| student_id_S4300 |        1.89243 |
| student_id_S4301 |       10.4597  |
| student_id_S4303 |       -1.08408 |
| student_id_S4305 |       -6.94072 |
| student_id_S4306 |       -8.33014 |
| student_id_S4307 |        1.23368 |
| student_id_S4308 |        7.55832 |
| student_id_S4309 |        9.5013  |
| student_id_S431  |       -1.97357 |

---

### Blocco 315 (Feature 3141 - 3150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4310 |       13.0647  |
| student_id_S4311 |       -3.19525 |
| student_id_S4312 |        7.82292 |
| student_id_S4313 |       -6.59666 |
| student_id_S4314 |      -12.4495  |
| student_id_S4315 |       10.1257  |
| student_id_S4316 |       11.6971  |
| student_id_S4317 |        3.66098 |
| student_id_S4318 |       -6.36459 |
| student_id_S4319 |       -2.79406 |

---

### Blocco 316 (Feature 3151 - 3160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S432  |       5.26384  |
| student_id_S4320 |       4.17648  |
| student_id_S4321 |       2.71843  |
| student_id_S4322 |      -0.547871 |
| student_id_S4323 |      -9.04164  |
| student_id_S4324 |     -10.8341   |
| student_id_S4325 |      -0.698091 |
| student_id_S4326 |      10.107    |
| student_id_S4327 |      -6.26243  |
| student_id_S433  |       3.18252  |

---

### Blocco 317 (Feature 3161 - 3170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4330 |      -0.230817 |
| student_id_S4331 |       9.33292  |
| student_id_S4332 |      -8.92134  |
| student_id_S4333 |      -0.944964 |
| student_id_S4334 |      -5.19706  |
| student_id_S4336 |     -15.4702   |
| student_id_S4338 |       9.17719  |
| student_id_S4339 |      11.736    |
| student_id_S434  |      -2.78894  |
| student_id_S4340 |       2.7279   |

---

### Blocco 318 (Feature 3171 - 3180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4341 |      -4.69085  |
| student_id_S4342 |      -5.79261  |
| student_id_S4343 |       7.47758  |
| student_id_S4344 |       8.71091  |
| student_id_S4345 |      -1.18557  |
| student_id_S4347 |      -5.61525  |
| student_id_S4348 |       0.667973 |
| student_id_S4349 |      -1.3186   |
| student_id_S435  |       1.09028  |
| student_id_S4350 |       9.65744  |

---

### Blocco 319 (Feature 3181 - 3190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4351 |       10.1091  |
| student_id_S4352 |       -5.22176 |
| student_id_S4354 |        2.10464 |
| student_id_S4355 |        1.63655 |
| student_id_S4357 |       -1.32641 |
| student_id_S4358 |        8.47661 |
| student_id_S436  |       12.7619  |
| student_id_S4360 |        1.15592 |
| student_id_S4361 |       -3.5756  |
| student_id_S4362 |       -4.79475 |

---

### Blocco 320 (Feature 3191 - 3200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4363 |      -5.12389  |
| student_id_S4364 |       1.96373  |
| student_id_S4365 |      10.8183   |
| student_id_S4366 |      13.8532   |
| student_id_S4367 |      11.6546   |
| student_id_S4368 |       0.573265 |
| student_id_S4369 |       9.17013  |
| student_id_S437  |       8.82192  |
| student_id_S4370 |       1.3984   |
| student_id_S4371 |      -4.59776  |

---

### Blocco 321 (Feature 3201 - 3210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4373 |       14.8505  |
| student_id_S4374 |       13.2497  |
| student_id_S4375 |        1.52635 |
| student_id_S4376 |       -8.04594 |
| student_id_S4377 |       -9.63817 |
| student_id_S4378 |       -4.51582 |
| student_id_S4379 |        2.44818 |
| student_id_S438  |       -7.2954  |
| student_id_S4380 |        1.76882 |
| student_id_S4383 |       -2.80766 |

---

### Blocco 322 (Feature 3211 - 3220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4384 |       5.09461  |
| student_id_S4385 |      -1.35603  |
| student_id_S4386 |      -4.42337  |
| student_id_S4387 |      -0.832662 |
| student_id_S4388 |       5.53835  |
| student_id_S4389 |     -12.2377   |
| student_id_S439  |       0.427572 |
| student_id_S4390 |       1.22924  |
| student_id_S4391 |      -6.47524  |
| student_id_S4392 |      -0.862689 |

---

### Blocco 323 (Feature 3221 - 3230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4393 |       8.78642  |
| student_id_S4394 |     -11.5233   |
| student_id_S4396 |      -4.10059  |
| student_id_S4399 |       0.284619 |
| student_id_S44   |       8.37875  |
| student_id_S440  |      -1.43741  |
| student_id_S4400 |      10.6089   |
| student_id_S4401 |       6.01307  |
| student_id_S4402 |       5.31967  |
| student_id_S4403 |      -5.13334  |

---

### Blocco 324 (Feature 3231 - 3240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4404 |       2.74858  |
| student_id_S4405 |      -8.29665  |
| student_id_S4406 |       7.61495  |
| student_id_S4408 |      -2.81626  |
| student_id_S4409 |       6.25396  |
| student_id_S441  |      13.5043   |
| student_id_S4410 |       5.20263  |
| student_id_S4412 |       0.266788 |
| student_id_S4413 |      -9.43778  |
| student_id_S4414 |       2.94836  |

---

### Blocco 325 (Feature 3241 - 3250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4415 |     -7.35067   |
| student_id_S4416 |      7.17682   |
| student_id_S4417 |    -13.5574    |
| student_id_S4418 |     -8.167     |
| student_id_S4419 |     -6.59289   |
| student_id_S442  |     -1.2325    |
| student_id_S4420 |     11.7873    |
| student_id_S4421 |      8.62284   |
| student_id_S4422 |     -1.84121   |
| student_id_S4423 |      0.0656229 |

---

### Blocco 326 (Feature 3251 - 3260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4424 |        8.77052 |
| student_id_S4425 |        8.10749 |
| student_id_S4426 |      -16.328   |
| student_id_S4427 |        3.7001  |
| student_id_S4428 |       -5.20333 |
| student_id_S4429 |       -8.67351 |
| student_id_S443  |        5.35053 |
| student_id_S4430 |       -9.7379  |
| student_id_S4431 |        7.0824  |
| student_id_S4432 |        5.56083 |

---

### Blocco 327 (Feature 3261 - 3270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4433 |       -7.30623 |
| student_id_S4434 |       -3.24016 |
| student_id_S4435 |       -4.13693 |
| student_id_S4437 |       13.6097  |
| student_id_S4438 |       12.0745  |
| student_id_S4439 |        3.76334 |
| student_id_S444  |        6.09234 |
| student_id_S4440 |      -11.4115  |
| student_id_S4441 |        5.04562 |
| student_id_S4442 |        3.24752 |

---

### Blocco 328 (Feature 3271 - 3280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4443 |      -10.7041  |
| student_id_S4444 |       -2.30724 |
| student_id_S4445 |       -6.91858 |
| student_id_S4446 |        4.8269  |
| student_id_S4447 |       -3.8778  |
| student_id_S4448 |        3.06688 |
| student_id_S4449 |       -7.21145 |
| student_id_S445  |        8.1093  |
| student_id_S4451 |       -7.8222  |
| student_id_S4452 |       -1.77527 |

---

### Blocco 329 (Feature 3281 - 3290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4453 |      -0.518157 |
| student_id_S4454 |      -8.76542  |
| student_id_S4455 |      -4.7497   |
| student_id_S4456 |      -7.58046  |
| student_id_S4457 |       5.87221  |
| student_id_S4458 |      -1.35844  |
| student_id_S4459 |       3.89562  |
| student_id_S446  |      -2.41406  |
| student_id_S4460 |      -4.46037  |
| student_id_S4461 |      11.4338   |

---

### Blocco 330 (Feature 3291 - 3300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4462 |        5.34128 |
| student_id_S4463 |       -5.06147 |
| student_id_S4464 |       -2.43547 |
| student_id_S4465 |        9.21679 |
| student_id_S4466 |        2.887   |
| student_id_S4467 |        9.4547  |
| student_id_S4468 |        6.16863 |
| student_id_S4469 |       -8.44928 |
| student_id_S447  |       -3.89372 |
| student_id_S4470 |       -0.73005 |

---

### Blocco 331 (Feature 3301 - 3310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4471 |      -5.95984  |
| student_id_S4472 |       2.52101  |
| student_id_S4473 |       3.08975  |
| student_id_S4474 |       8.46261  |
| student_id_S4476 |       8.51965  |
| student_id_S4477 |       6.35165  |
| student_id_S4478 |      -2.84093  |
| student_id_S4479 |       6.86645  |
| student_id_S448  |       0.278877 |
| student_id_S4480 |       3.48587  |

---

### Blocco 332 (Feature 3311 - 3320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4481 |     -11.901    |
| student_id_S4482 |      -6.44187  |
| student_id_S4483 |       2.57427  |
| student_id_S4484 |       2.17028  |
| student_id_S4485 |     -12.7706   |
| student_id_S4486 |      -3.06213  |
| student_id_S4487 |       1.7579   |
| student_id_S4489 |       0.962924 |
| student_id_S449  |     -13.2561   |
| student_id_S4490 |       6.89483  |

---

### Blocco 333 (Feature 3321 - 3330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4493 |      -1.30188  |
| student_id_S4494 |      -0.655789 |
| student_id_S4495 |       7.83591  |
| student_id_S4496 |       2.79203  |
| student_id_S4497 |      -3.47649  |
| student_id_S4498 |       2.80864  |
| student_id_S4499 |     -12.2545   |
| student_id_S45   |       1.74707  |
| student_id_S4500 |       6.71032  |
| student_id_S4501 |      -6.37733  |

---

### Blocco 334 (Feature 3331 - 3340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4502 |      -8.06135  |
| student_id_S4503 |      -3.95873  |
| student_id_S4504 |       4.09368  |
| student_id_S4505 |      -3.52073  |
| student_id_S4506 |      -3.19212  |
| student_id_S4507 |      13.8372   |
| student_id_S4508 |      -8.69372  |
| student_id_S4509 |       0.127729 |
| student_id_S451  |      -2.34367  |
| student_id_S4510 |       3.58573  |

---

### Blocco 335 (Feature 3341 - 3350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4511 |       4.332    |
| student_id_S4512 |       0.686395 |
| student_id_S4513 |      -6.39192  |
| student_id_S4514 |      -0.605347 |
| student_id_S4516 |       6.27952  |
| student_id_S4518 |      -0.351766 |
| student_id_S4519 |      -7.10201  |
| student_id_S452  |       7.40891  |
| student_id_S4520 |       4.75562  |
| student_id_S4521 |      -6.42724  |

---

### Blocco 336 (Feature 3351 - 3360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4522 |        2.8858  |
| student_id_S4524 |       11.8005  |
| student_id_S4525 |       11.6064  |
| student_id_S4526 |        2.95192 |
| student_id_S4527 |        1.67102 |
| student_id_S4528 |        8.73139 |
| student_id_S453  |       -3.02837 |
| student_id_S4531 |        2.53686 |
| student_id_S4532 |        9.00227 |
| student_id_S4533 |       11.1925  |

---

### Blocco 337 (Feature 3361 - 3370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4534 |       -7.87313 |
| student_id_S4535 |       -6.97454 |
| student_id_S4536 |       14.4324  |
| student_id_S4537 |      -10.9628  |
| student_id_S4538 |       12.8467  |
| student_id_S454  |        9.43338 |
| student_id_S4540 |      -11.1413  |
| student_id_S4541 |        2.05902 |
| student_id_S4542 |        9.97808 |
| student_id_S4543 |        3.33514 |

---

### Blocco 338 (Feature 3371 - 3380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4545 |      11.2042   |
| student_id_S4546 |       2.9819   |
| student_id_S4547 |       0.302599 |
| student_id_S4548 |       2.41993  |
| student_id_S4549 |       0.767489 |
| student_id_S4550 |       0.146303 |
| student_id_S4551 |      -2.07539  |
| student_id_S4552 |      -6.54531  |
| student_id_S4553 |      -7.72776  |
| student_id_S4554 |       2.73395  |

---

### Blocco 339 (Feature 3381 - 3390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4555 |       -6.59764 |
| student_id_S4557 |       12.319   |
| student_id_S4558 |       -1.54392 |
| student_id_S4559 |       12.7162  |
| student_id_S456  |       -2.76247 |
| student_id_S4560 |        1.80583 |
| student_id_S4561 |       -1.17868 |
| student_id_S4562 |      -10.2456  |
| student_id_S4564 |      -11.0237  |
| student_id_S4565 |       11.4591  |

---

### Blocco 340 (Feature 3391 - 3400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4566 |      -3.1892   |
| student_id_S4567 |      -1.7974   |
| student_id_S4568 |      -6.64581  |
| student_id_S4569 |       3.83037  |
| student_id_S457  |       6.12438  |
| student_id_S4570 |       1.55897  |
| student_id_S4571 |      -3.97054  |
| student_id_S4572 |       3.32873  |
| student_id_S4573 |      -0.416564 |
| student_id_S4574 |       1.76305  |

---

### Blocco 341 (Feature 3401 - 3410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4575 |       -5.37425 |
| student_id_S4577 |        0.45967 |
| student_id_S4578 |        1.79553 |
| student_id_S458  |       10.4891  |
| student_id_S4582 |        5.5454  |
| student_id_S4583 |       -4.46028 |
| student_id_S4585 |        5.95953 |
| student_id_S4586 |       -1.61785 |
| student_id_S4587 |       -4.94774 |
| student_id_S4588 |       -6.63407 |

---

### Blocco 342 (Feature 3411 - 3420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4589 |       9.83851  |
| student_id_S459  |       7.67634  |
| student_id_S4590 |      13.9109   |
| student_id_S4591 |      -0.140179 |
| student_id_S4592 |      -1.814    |
| student_id_S4594 |       7.75078  |
| student_id_S4595 |      13.1321   |
| student_id_S4596 |      -1.22768  |
| student_id_S4597 |      -1.83525  |
| student_id_S4598 |     -12.3522   |

---

### Blocco 343 (Feature 3421 - 3430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S460  |        5.31252 |
| student_id_S4600 |       -4.27273 |
| student_id_S4601 |        4.18849 |
| student_id_S4602 |       10.4464  |
| student_id_S4603 |        9.61988 |
| student_id_S4604 |        4.29335 |
| student_id_S4605 |       -4.19862 |
| student_id_S4606 |        1.30425 |
| student_id_S4608 |       12.6684  |
| student_id_S4609 |       -1.25178 |

---

### Blocco 344 (Feature 3431 - 3440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S461  |      1.63529   |
| student_id_S4610 |      7.01864   |
| student_id_S4611 |     12.0899    |
| student_id_S4612 |     -0.997564  |
| student_id_S4614 |     -2.58524   |
| student_id_S4615 |      9.52484   |
| student_id_S4616 |     -0.988668  |
| student_id_S4617 |      0.974165  |
| student_id_S4618 |     -2.67863   |
| student_id_S4619 |     -0.0400876 |

---

### Blocco 345 (Feature 3441 - 3450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S462  |     -3.03135   |
| student_id_S4620 |      5.01595   |
| student_id_S4621 |      2.82806   |
| student_id_S4623 |     -4.75273   |
| student_id_S4624 |      9.41565   |
| student_id_S4625 |     -5.51609   |
| student_id_S4626 |      1.32221   |
| student_id_S4627 |      6.99015   |
| student_id_S4628 |     -4.77906   |
| student_id_S4629 |      0.0938609 |

---

### Blocco 346 (Feature 3451 - 3460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S463  |      -4.33683  |
| student_id_S4630 |      -1.71796  |
| student_id_S4631 |       8.28098  |
| student_id_S4632 |     -13.75     |
| student_id_S4633 |       6.75902  |
| student_id_S4634 |       0.311036 |
| student_id_S4635 |       9.88538  |
| student_id_S4636 |      -5.60764  |
| student_id_S4637 |      -6.0094   |
| student_id_S4638 |      -0.827086 |

---

### Blocco 347 (Feature 3461 - 3470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4639 |      -1.93023  |
| student_id_S4640 |       2.05706  |
| student_id_S4641 |      10.7635   |
| student_id_S4642 |       7.89854  |
| student_id_S4643 |      -6.17269  |
| student_id_S4644 |      -4.74794  |
| student_id_S4647 |       3.7351   |
| student_id_S4648 |       4.24579  |
| student_id_S4649 |      -7.79891  |
| student_id_S465  |       0.407475 |

---

### Blocco 348 (Feature 3471 - 3480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4650 |        9.65839 |
| student_id_S4651 |       11.676   |
| student_id_S4652 |       -8.60623 |
| student_id_S4653 |        9.81784 |
| student_id_S4655 |       -1.33867 |
| student_id_S4656 |      -13.2509  |
| student_id_S4657 |       -8.54185 |
| student_id_S4658 |       -0.37453 |
| student_id_S4659 |        7.17544 |
| student_id_S466  |       -3.83567 |

---

### Blocco 349 (Feature 3481 - 3490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4660 |       1.16406  |
| student_id_S4661 |       5.22714  |
| student_id_S4662 |       7.96897  |
| student_id_S4663 |      -8.29043  |
| student_id_S4664 |      -5.93915  |
| student_id_S4665 |       9.28729  |
| student_id_S4666 |       0.404517 |
| student_id_S4668 |      -7.77799  |
| student_id_S4669 |      -2.23842  |
| student_id_S467  |      -3.15185  |

---

### Blocco 350 (Feature 3491 - 3500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4670 |      11.4876   |
| student_id_S4671 |       1.45417  |
| student_id_S4672 |      -1.69728  |
| student_id_S4673 |      -2.06495  |
| student_id_S4674 |      -0.678921 |
| student_id_S4677 |       2.71692  |
| student_id_S4678 |       5.35087  |
| student_id_S4679 |      10.6921   |
| student_id_S468  |       6.66186  |
| student_id_S4681 |      -6.4853   |

---

### Blocco 351 (Feature 3501 - 3510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4683 |       -6.48894 |
| student_id_S4684 |       -2.69956 |
| student_id_S4685 |       -6.28832 |
| student_id_S4686 |        6.44124 |
| student_id_S4688 |        4.69469 |
| student_id_S4689 |       -7.96072 |
| student_id_S469  |        1.18894 |
| student_id_S4690 |       -4.00206 |
| student_id_S4691 |       -5.68225 |
| student_id_S4692 |        2.50247 |

---

### Blocco 352 (Feature 3511 - 3520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4693 |       0.976227 |
| student_id_S4694 |      -0.870674 |
| student_id_S4695 |      -1.12599  |
| student_id_S4696 |       3.74466  |
| student_id_S4697 |       5.5778   |
| student_id_S4698 |      -7.41535  |
| student_id_S4699 |      11.3887   |
| student_id_S47   |       0.904642 |
| student_id_S470  |      -3.82072  |
| student_id_S4700 |      -3.7356   |

---

### Blocco 353 (Feature 3521 - 3530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4701 |      3.877     |
| student_id_S4702 |      9.4768    |
| student_id_S4703 |     -8.48859   |
| student_id_S4706 |      5.70082   |
| student_id_S4708 |     -0.107865  |
| student_id_S4709 |      6.1914    |
| student_id_S471  |     -8.49561   |
| student_id_S4711 |      1.42614   |
| student_id_S4712 |     -8.01735   |
| student_id_S4713 |      0.0603254 |

---

### Blocco 354 (Feature 3531 - 3540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4714 |       6.0621   |
| student_id_S4715 |      -0.737814 |
| student_id_S4716 |       7.59561  |
| student_id_S4717 |      -3.5998   |
| student_id_S4718 |       1.24859  |
| student_id_S4719 |      -5.07951  |
| student_id_S472  |     -14.1361   |
| student_id_S4720 |      -0.348886 |
| student_id_S4721 |      -6.87357  |
| student_id_S4722 |       5.04108  |

---

### Blocco 355 (Feature 3541 - 3550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4724 |     -6.42281   |
| student_id_S4725 |      3.91668   |
| student_id_S4727 |     -2.53644   |
| student_id_S4728 |      4.20026   |
| student_id_S4729 |      3.0596    |
| student_id_S473  |      2.76356   |
| student_id_S4730 |     -2.97171   |
| student_id_S4731 |     -0.0572173 |
| student_id_S4732 |     -9.42956   |
| student_id_S4733 |     -1.71834   |

---

### Blocco 356 (Feature 3551 - 3560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4735 |       7.31732  |
| student_id_S4737 |      -4.11731  |
| student_id_S4738 |      18.7878   |
| student_id_S4739 |      14.5353   |
| student_id_S474  |      15.5053   |
| student_id_S4742 |      -9.83497  |
| student_id_S4743 |      -1.39461  |
| student_id_S4744 |       0.602184 |
| student_id_S4746 |       8.6565   |
| student_id_S4747 |      -0.439697 |

---

### Blocco 357 (Feature 3561 - 3570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4748 |      -6.42668  |
| student_id_S4749 |     -14.9133   |
| student_id_S475  |      -1.30757  |
| student_id_S4750 |       4.66271  |
| student_id_S4751 |       6.26312  |
| student_id_S4752 |       0.12614  |
| student_id_S4753 |       7.975    |
| student_id_S4756 |      -0.619163 |
| student_id_S4757 |       9.15809  |
| student_id_S4758 |       5.15598  |

---

### Blocco 358 (Feature 3571 - 3580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4759 |        1.52244 |
| student_id_S476  |        1.59686 |
| student_id_S4760 |      -14.6945  |
| student_id_S4761 |       -1.67781 |
| student_id_S4762 |       -4.422   |
| student_id_S4763 |        7.18404 |
| student_id_S4765 |       -4.07705 |
| student_id_S4767 |       11.4183  |
| student_id_S4768 |       -2.23059 |
| student_id_S4769 |       11.8081  |

---

### Blocco 359 (Feature 3581 - 3590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S477  |       -3.04122 |
| student_id_S4770 |       -8.53716 |
| student_id_S4771 |        8.61682 |
| student_id_S4772 |        7.51964 |
| student_id_S4773 |       -2.91995 |
| student_id_S4774 |       -3.041   |
| student_id_S4775 |        1.31017 |
| student_id_S4776 |       -7.7473  |
| student_id_S4777 |        8.72605 |
| student_id_S4778 |        5.27697 |

---

### Blocco 360 (Feature 3591 - 3600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4779 |       6.32168  |
| student_id_S478  |       4.90603  |
| student_id_S4780 |       0.728586 |
| student_id_S4782 |      -6.35756  |
| student_id_S4783 |       1.40305  |
| student_id_S4784 |       0.406113 |
| student_id_S4785 |      12.255    |
| student_id_S4786 |       2.11468  |
| student_id_S4787 |       3.76681  |
| student_id_S4788 |       6.63638  |

---

### Blocco 361 (Feature 3601 - 3610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S479  |      -0.774839 |
| student_id_S4790 |      -0.343029 |
| student_id_S4792 |       4.89898  |
| student_id_S4794 |       0.500293 |
| student_id_S4795 |       2.97753  |
| student_id_S4796 |      -5.08161  |
| student_id_S4797 |       4.63995  |
| student_id_S4798 |       7.93744  |
| student_id_S4799 |      -5.03972  |
| student_id_S4800 |      -6.34875  |

---

### Blocco 362 (Feature 3611 - 3620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4801 |       4.49923  |
| student_id_S4802 |      -0.510459 |
| student_id_S4803 |     -11.4081   |
| student_id_S4804 |      -1.6512   |
| student_id_S4805 |      -7.80041  |
| student_id_S4806 |       6.44993  |
| student_id_S4807 |       7.17369  |
| student_id_S4808 |       3.98886  |
| student_id_S4809 |       3.4812   |
| student_id_S481  |      -1.50643  |

---

### Blocco 363 (Feature 3621 - 3630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4810 |      -0.781281 |
| student_id_S4811 |       0.684679 |
| student_id_S4812 |      -2.058    |
| student_id_S4813 |      -3.94519  |
| student_id_S4814 |      13.9073   |
| student_id_S4816 |       6.57783  |
| student_id_S4818 |       6.35567  |
| student_id_S4819 |      -0.10487  |
| student_id_S482  |      -1.35892  |
| student_id_S4820 |      -5.97306  |

---

### Blocco 364 (Feature 3631 - 3640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4821 |       1.02325  |
| student_id_S4823 |      -7.47839  |
| student_id_S4824 |      17.1625   |
| student_id_S4825 |      -6.30319  |
| student_id_S4826 |       4.6396   |
| student_id_S4827 |       0.417439 |
| student_id_S4828 |      -2.56717  |
| student_id_S4829 |      -7.64884  |
| student_id_S483  |       2.45381  |
| student_id_S4830 |      -9.06379  |

---

### Blocco 365 (Feature 3641 - 3650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4831 |     -12.3049   |
| student_id_S4832 |       3.82446  |
| student_id_S4833 |       0.821621 |
| student_id_S4834 |      -0.514164 |
| student_id_S4835 |       7.46199  |
| student_id_S4836 |       3.10885  |
| student_id_S4837 |     -12.8344   |
| student_id_S4839 |       8.35514  |
| student_id_S484  |       8.92927  |
| student_id_S4840 |      -8.84516  |

---

### Blocco 366 (Feature 3651 - 3660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4841 |      4.67461   |
| student_id_S4842 |     -6.26083   |
| student_id_S4843 |      7.30561   |
| student_id_S4846 |     15.9913    |
| student_id_S4848 |     -6.76288   |
| student_id_S4849 |     -7.26845   |
| student_id_S485  |     -3.07434   |
| student_id_S4850 |      5.44188   |
| student_id_S4851 |     -0.0307764 |
| student_id_S4852 |     -2.542     |

---

### Blocco 367 (Feature 3661 - 3670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4853 |     -7.64781   |
| student_id_S4854 |     -2.13203   |
| student_id_S4855 |     -6.11121   |
| student_id_S4856 |      3.42681   |
| student_id_S4857 |      9.23542   |
| student_id_S4858 |      1.18317   |
| student_id_S4859 |      4.24766   |
| student_id_S486  |     -9.48715   |
| student_id_S4862 |      0.0541602 |
| student_id_S4863 |    -10.583     |

---

### Blocco 368 (Feature 3671 - 3680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4864 |      -13.7073  |
| student_id_S4865 |       10.7643  |
| student_id_S4867 |       -4.18669 |
| student_id_S4868 |        4.36976 |
| student_id_S4870 |       10.9335  |
| student_id_S4871 |        7.98231 |
| student_id_S4872 |        2.00161 |
| student_id_S4873 |       -2.18741 |
| student_id_S4874 |        5.66031 |
| student_id_S4875 |       -6.06294 |

---

### Blocco 369 (Feature 3681 - 3690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4876 |       0.6462   |
| student_id_S4877 |      -3.58455  |
| student_id_S4878 |      -2.74336  |
| student_id_S4879 |      -1.65952  |
| student_id_S488  |      -6.15007  |
| student_id_S4880 |       3.74555  |
| student_id_S4881 |       0.389169 |
| student_id_S4882 |       6.8051   |
| student_id_S4883 |       3.99252  |
| student_id_S4884 |      -7.37754  |

---

### Blocco 370 (Feature 3691 - 3700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4885 |       1.70677  |
| student_id_S4886 |       1.20412  |
| student_id_S4887 |      -5.88477  |
| student_id_S4889 |       5.1727   |
| student_id_S489  |       0.815457 |
| student_id_S4890 |      -1.22177  |
| student_id_S4891 |      -4.40083  |
| student_id_S4893 |     -16.0074   |
| student_id_S4894 |      -0.78548  |
| student_id_S4895 |      -2.98808  |

---

### Blocco 371 (Feature 3701 - 3710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4896 |       1.92524  |
| student_id_S4898 |       0.680704 |
| student_id_S4899 |      -5.82215  |
| student_id_S49   |      -3.26636  |
| student_id_S490  |       6.94602  |
| student_id_S4900 |       1.85818  |
| student_id_S4901 |       7.89044  |
| student_id_S4903 |     -14.4531   |
| student_id_S4904 |     -10.1622   |
| student_id_S4905 |       6.9204   |

---

### Blocco 372 (Feature 3711 - 3720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4906 |       11.8318  |
| student_id_S4907 |        2.9686  |
| student_id_S4908 |       -5.10642 |
| student_id_S4909 |       10.6256  |
| student_id_S491  |       -5.7921  |
| student_id_S4911 |       -4.69078 |
| student_id_S4912 |       -8.72159 |
| student_id_S4913 |        1.60978 |
| student_id_S4914 |        7.97657 |
| student_id_S4915 |       -4.09838 |

---

### Blocco 373 (Feature 3721 - 3730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4916 |       7.82661  |
| student_id_S4917 |      -8.18293  |
| student_id_S4918 |      -4.72599  |
| student_id_S4919 |       9.29982  |
| student_id_S492  |     -10.2242   |
| student_id_S4920 |      -4.46155  |
| student_id_S4921 |       9.27824  |
| student_id_S4922 |       3.41509  |
| student_id_S4923 |       9.36156  |
| student_id_S4924 |       0.534226 |

---

### Blocco 374 (Feature 3731 - 3740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4926 |       6.28555  |
| student_id_S4927 |      -5.45712  |
| student_id_S4928 |       0.605989 |
| student_id_S4929 |       4.41931  |
| student_id_S493  |       8.47915  |
| student_id_S4930 |       2.74279  |
| student_id_S4931 |      -6.16826  |
| student_id_S4932 |      -6.60065  |
| student_id_S4933 |       7.19768  |
| student_id_S4934 |      -0.20366  |

---

### Blocco 375 (Feature 3741 - 3750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4935 |     -1.36509   |
| student_id_S4936 |    -10.9691    |
| student_id_S4937 |      0.0967872 |
| student_id_S4938 |     11.5612    |
| student_id_S494  |     -5.19943   |
| student_id_S4940 |    -12.3604    |
| student_id_S4941 |      4.23989   |
| student_id_S4942 |     -3.74622   |
| student_id_S4943 |     -5.06977   |
| student_id_S4944 |     -9.16282   |

---

### Blocco 376 (Feature 3751 - 3760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4945 |       7.77529  |
| student_id_S4946 |     -10.689    |
| student_id_S4948 |      -6.47482  |
| student_id_S495  |       2.16922  |
| student_id_S4950 |       0.532022 |
| student_id_S4951 |       5.66564  |
| student_id_S4953 |     -10.2215   |
| student_id_S4954 |       9.1327   |
| student_id_S4955 |      -0.781585 |
| student_id_S4957 |      -0.679843 |

---

### Blocco 377 (Feature 3761 - 3770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4958 |       1.95195  |
| student_id_S4959 |      -3.57805  |
| student_id_S496  |      -0.891978 |
| student_id_S4960 |      -6.79573  |
| student_id_S4961 |       0.821706 |
| student_id_S4962 |       0.72075  |
| student_id_S4963 |       2.05846  |
| student_id_S4964 |      -1.65129  |
| student_id_S4967 |      11.9294   |
| student_id_S4968 |      -2.99509  |

---

### Blocco 378 (Feature 3771 - 3780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4969 |      -1.92741  |
| student_id_S4970 |       9.60833  |
| student_id_S4971 |       0.234375 |
| student_id_S4974 |       4.93064  |
| student_id_S4975 |       6.68038  |
| student_id_S4976 |      -1.9627   |
| student_id_S4977 |      -1.00199  |
| student_id_S4978 |       0.805043 |
| student_id_S4979 |      -0.802151 |
| student_id_S498  |      13.3713   |

---

### Blocco 379 (Feature 3781 - 3790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4980 |       -9.68033 |
| student_id_S4981 |        1.98515 |
| student_id_S4982 |        9.02528 |
| student_id_S4983 |       -2.75124 |
| student_id_S4984 |        2.10918 |
| student_id_S4986 |        7.75168 |
| student_id_S4987 |        6.80065 |
| student_id_S4988 |       15.151   |
| student_id_S4989 |        9.53054 |
| student_id_S499  |       -1.54588 |

---

### Blocco 380 (Feature 3791 - 3800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S4990 |       15.025   |
| student_id_S4991 |       -3.88537 |
| student_id_S4992 |      -12.9474  |
| student_id_S4993 |       -1.71399 |
| student_id_S4994 |        4.11495 |
| student_id_S4996 |       -8.69346 |
| student_id_S4997 |        2.45839 |
| student_id_S4998 |      -10.5696  |
| student_id_S5    |        2.30854 |
| student_id_S50   |       -2.91751 |

---

### Blocco 381 (Feature 3801 - 3810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S500  |        6.45199 |
| student_id_S5000 |       -6.43537 |
| student_id_S5002 |       -9.9404  |
| student_id_S5003 |       -1.37959 |
| student_id_S5004 |        5.46074 |
| student_id_S5005 |       -1.77591 |
| student_id_S5006 |       -9.28848 |
| student_id_S5007 |        4.06036 |
| student_id_S5008 |        6.61043 |
| student_id_S5009 |       -8.14394 |

---

### Blocco 382 (Feature 3811 - 3820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5010 |        6.20423 |
| student_id_S5012 |       -7.97826 |
| student_id_S5013 |        1.81883 |
| student_id_S5015 |        8.44794 |
| student_id_S5016 |        5.21912 |
| student_id_S5017 |      -12.1307  |
| student_id_S5019 |        8.04072 |
| student_id_S502  |       -2.73334 |
| student_id_S5021 |       -7.63584 |
| student_id_S5022 |        3.16414 |

---

### Blocco 383 (Feature 3821 - 3830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5023 |        5.9263  |
| student_id_S5024 |        4.6427  |
| student_id_S5025 |       -3.30685 |
| student_id_S5026 |        8.49593 |
| student_id_S5028 |       -3.38736 |
| student_id_S5032 |        5.37313 |
| student_id_S5033 |      -10.739   |
| student_id_S5034 |      -14.2458  |
| student_id_S5035 |        6.0703  |
| student_id_S5036 |       -2.06424 |

---

### Blocco 384 (Feature 3831 - 3840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5037 |       8.51137  |
| student_id_S5038 |      -0.270832 |
| student_id_S5039 |      -2.95688  |
| student_id_S504  |       9.0011   |
| student_id_S5040 |      -2.58082  |
| student_id_S5041 |     -12.8797   |
| student_id_S5042 |      -1.71231  |
| student_id_S5043 |       7.90322  |
| student_id_S5044 |       8.32304  |
| student_id_S5045 |       2.92474  |

---

### Blocco 385 (Feature 3841 - 3850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5046 |      -10.1902  |
| student_id_S5047 |        1.87134 |
| student_id_S5048 |       -5.0071  |
| student_id_S5049 |        8.01023 |
| student_id_S505  |       -6.64577 |
| student_id_S5052 |       -4.04551 |
| student_id_S5053 |        6.72385 |
| student_id_S5054 |       -8.47506 |
| student_id_S5055 |      -11.2422  |
| student_id_S5056 |       -8.52286 |

---

### Blocco 386 (Feature 3851 - 3860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5057 |      -10.7805  |
| student_id_S5059 |       -7.4273  |
| student_id_S506  |        3.49937 |
| student_id_S5060 |       11.1423  |
| student_id_S5061 |       -5.07916 |
| student_id_S5062 |        4.03927 |
| student_id_S5063 |        2.31888 |
| student_id_S5064 |       -5.73404 |
| student_id_S5065 |       -4.64054 |
| student_id_S5066 |       -4.21506 |

---

### Blocco 387 (Feature 3861 - 3870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5067 |       -1.06919 |
| student_id_S5068 |       11.8282  |
| student_id_S5069 |        5.50497 |
| student_id_S507  |       13.5837  |
| student_id_S5070 |        5.40803 |
| student_id_S5071 |       -5.40167 |
| student_id_S5072 |       11.5516  |
| student_id_S5073 |        3.18469 |
| student_id_S5076 |        4.20068 |
| student_id_S5077 |        1.439   |

---

### Blocco 388 (Feature 3871 - 3880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5079 |       6.59722  |
| student_id_S508  |       6.54184  |
| student_id_S5080 |      -0.438809 |
| student_id_S5081 |      -3.50467  |
| student_id_S5082 |       6.84429  |
| student_id_S5083 |      -0.271296 |
| student_id_S5085 |      -2.98606  |
| student_id_S5086 |       0.140452 |
| student_id_S5087 |      -4.43404  |
| student_id_S5088 |       6.66276  |

---

### Blocco 389 (Feature 3881 - 3890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5089 |      -6.22402  |
| student_id_S509  |      -0.531325 |
| student_id_S5090 |       5.32352  |
| student_id_S5091 |      -3.90933  |
| student_id_S5092 |      -4.26142  |
| student_id_S5093 |       6.8246   |
| student_id_S5094 |      -9.06663  |
| student_id_S5095 |       2.45668  |
| student_id_S5096 |      -1.25746  |
| student_id_S5097 |       7.49075  |

---

### Blocco 390 (Feature 3891 - 3900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5098 |      -1.69484  |
| student_id_S5099 |       5.6471   |
| student_id_S51   |      -8.70106  |
| student_id_S510  |      -6.11986  |
| student_id_S5100 |       0.644312 |
| student_id_S5101 |      -0.72656  |
| student_id_S5102 |      -8.07529  |
| student_id_S5103 |     -11.6521   |
| student_id_S5104 |      -1.75085  |
| student_id_S5105 |      -0.53763  |

---

### Blocco 391 (Feature 3901 - 3910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5107 |        2.6956  |
| student_id_S5108 |        5.25302 |
| student_id_S5110 |       -7.00459 |
| student_id_S5111 |        0.96093 |
| student_id_S5112 |        5.62194 |
| student_id_S5113 |       -6.13295 |
| student_id_S5114 |       -2.95127 |
| student_id_S5115 |        6.94624 |
| student_id_S5116 |        4.45382 |
| student_id_S5117 |       13.6756  |

---

### Blocco 392 (Feature 3911 - 3920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5118 |       1.57169  |
| student_id_S5119 |      11.8337   |
| student_id_S512  |       8.27331  |
| student_id_S5120 |       8.68267  |
| student_id_S5121 |       8.95295  |
| student_id_S5122 |      -4.2482   |
| student_id_S5123 |      -0.997773 |
| student_id_S5126 |       3.68016  |
| student_id_S5127 |       3.04188  |
| student_id_S5129 |       0.573739 |

---

### Blocco 393 (Feature 3921 - 3930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S513  |       -4.47665 |
| student_id_S5130 |       -2.29246 |
| student_id_S5131 |       -6.4912  |
| student_id_S5132 |       -4.53156 |
| student_id_S5133 |       -5.61174 |
| student_id_S5134 |       -6.30409 |
| student_id_S5135 |        4.25259 |
| student_id_S5136 |        8.40546 |
| student_id_S5137 |       -5.37928 |
| student_id_S5138 |        3.72573 |

---

### Blocco 394 (Feature 3931 - 3940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S514  |       6.43873  |
| student_id_S5140 |       8.62171  |
| student_id_S5141 |      -2.32254  |
| student_id_S5142 |      -0.562467 |
| student_id_S5143 |       9.3085   |
| student_id_S5144 |      -7.58979  |
| student_id_S5146 |       1.77687  |
| student_id_S5147 |      -5.2134   |
| student_id_S5148 |       0.190767 |
| student_id_S5150 |       5.12535  |

---

### Blocco 395 (Feature 3941 - 3950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5151 |       1.71895  |
| student_id_S5152 |      -3.10586  |
| student_id_S5153 |       0.307701 |
| student_id_S5154 |      -3.28714  |
| student_id_S5155 |      -4.27528  |
| student_id_S5156 |       0.820701 |
| student_id_S5158 |      -8.77872  |
| student_id_S5159 |       8.14793  |
| student_id_S516  |      11.6295   |
| student_id_S5161 |     -10.3137   |

---

### Blocco 396 (Feature 3951 - 3960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5162 |     10.7511    |
| student_id_S5163 |      4.42254   |
| student_id_S5164 |     -0.349419  |
| student_id_S5165 |      8.94512   |
| student_id_S5166 |      8.89841   |
| student_id_S5167 |      2.55543   |
| student_id_S5168 |      9.16348   |
| student_id_S517  |      0.0579212 |
| student_id_S5170 |     14.2439    |
| student_id_S5172 |     -8.24557   |

---

### Blocco 397 (Feature 3961 - 3970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5173 |       9.89884  |
| student_id_S5174 |      13.7286   |
| student_id_S5176 |       0.598969 |
| student_id_S5178 |      -3.78025  |
| student_id_S5179 |       5.04176  |
| student_id_S518  |       6.51155  |
| student_id_S5180 |       4.84421  |
| student_id_S5181 |       4.46472  |
| student_id_S5184 |      13.3997   |
| student_id_S5185 |       5.04873  |

---

### Blocco 398 (Feature 3971 - 3980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5186 |       0.443819 |
| student_id_S5187 |      -3.34983  |
| student_id_S5188 |       4.7867   |
| student_id_S5189 |      -3.94645  |
| student_id_S519  |       7.23207  |
| student_id_S5190 |       6.77827  |
| student_id_S5191 |       5.71455  |
| student_id_S5192 |     -12.0588   |
| student_id_S5194 |      -3.45261  |
| student_id_S5195 |      13.2929   |

---

### Blocco 399 (Feature 3981 - 3990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5197 |      -5.32462  |
| student_id_S5198 |      -7.31175  |
| student_id_S5199 |       4.95207  |
| student_id_S52   |      -0.703149 |
| student_id_S520  |       8.65804  |
| student_id_S5200 |       0.714053 |
| student_id_S5201 |       6.5113   |
| student_id_S5202 |      -4.19823  |
| student_id_S5203 |       1.36568  |
| student_id_S5205 |       6.25939  |

---

### Blocco 400 (Feature 3991 - 4000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5206 |      -7.08832  |
| student_id_S5207 |      -2.13319  |
| student_id_S5208 |      11.5692   |
| student_id_S5209 |      -3.58203  |
| student_id_S521  |     -12.3663   |
| student_id_S5210 |      -5.25133  |
| student_id_S5211 |       3.23545  |
| student_id_S5212 |      -0.324966 |
| student_id_S5213 |      -9.32417  |
| student_id_S5214 |      -4.22574  |

---

### Blocco 401 (Feature 4001 - 4010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5215 |       -9.24511 |
| student_id_S5217 |        4.93571 |
| student_id_S5218 |       12.4461  |
| student_id_S5219 |       -5.56299 |
| student_id_S5221 |        4.50405 |
| student_id_S5222 |        5.50834 |
| student_id_S5223 |       -8.64924 |
| student_id_S5224 |       -1.10326 |
| student_id_S5225 |        3.62176 |
| student_id_S5226 |        6.90061 |

---

### Blocco 402 (Feature 4011 - 4020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5227 |       -2.39292 |
| student_id_S523  |        9.19614 |
| student_id_S5230 |        2.2739  |
| student_id_S5231 |       -8.60725 |
| student_id_S5232 |        5.37185 |
| student_id_S5234 |       -2.15016 |
| student_id_S5235 |        3.05607 |
| student_id_S5236 |        4.33044 |
| student_id_S5237 |        8.62256 |
| student_id_S5238 |       -3.18152 |

---

### Blocco 403 (Feature 4021 - 4030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S524  |       -4.01597 |
| student_id_S5240 |        4.77413 |
| student_id_S5241 |       -4.09336 |
| student_id_S5243 |        1.29216 |
| student_id_S5244 |       -9.53442 |
| student_id_S5245 |        5.86936 |
| student_id_S5246 |       13.144   |
| student_id_S5248 |       12.0594  |
| student_id_S5249 |        4.02927 |
| student_id_S525  |        7.72657 |

---

### Blocco 404 (Feature 4031 - 4040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5250 |        7.12109 |
| student_id_S5251 |       19.8043  |
| student_id_S5252 |        1.98624 |
| student_id_S5253 |        1.94936 |
| student_id_S5254 |       -3.74224 |
| student_id_S5255 |        5.36297 |
| student_id_S5256 |        3.96193 |
| student_id_S5257 |        5.08208 |
| student_id_S5258 |      -10.113   |
| student_id_S5259 |       -2.93808 |

---

### Blocco 405 (Feature 4041 - 4050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S526  |       7.22662  |
| student_id_S5260 |       1.94115  |
| student_id_S5261 |       1.44061  |
| student_id_S5262 |       1.79916  |
| student_id_S5263 |       8.20404  |
| student_id_S5264 |       0.629137 |
| student_id_S5265 |      -8.61338  |
| student_id_S5266 |      11.1742   |
| student_id_S5267 |      -6.0116   |
| student_id_S5268 |      -1.25723  |

---

### Blocco 406 (Feature 4051 - 4060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5269 |      -6.65589  |
| student_id_S527  |      -0.657919 |
| student_id_S5271 |      -2.75026  |
| student_id_S5272 |      -8.69939  |
| student_id_S5273 |       0.363494 |
| student_id_S5274 |      -3.73316  |
| student_id_S5275 |     -10.2428   |
| student_id_S5277 |       8.59486  |
| student_id_S5278 |      -2.65882  |
| student_id_S5279 |       8.75643  |

---

### Blocco 407 (Feature 4061 - 4070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S528  |     -12.4139   |
| student_id_S5280 |       6.68749  |
| student_id_S5282 |      -7.96921  |
| student_id_S5283 |      -6.75276  |
| student_id_S5284 |      -8.3607   |
| student_id_S5285 |       6.82815  |
| student_id_S5287 |       0.479845 |
| student_id_S5288 |       8.45869  |
| student_id_S5289 |       1.92126  |
| student_id_S529  |      -0.543874 |

---

### Blocco 408 (Feature 4071 - 4080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5290 |        8.40962 |
| student_id_S5291 |        2.16327 |
| student_id_S5292 |       -6.34025 |
| student_id_S5293 |       -1.83057 |
| student_id_S5294 |        4.31877 |
| student_id_S5295 |        2.33665 |
| student_id_S5296 |      -12.368   |
| student_id_S5297 |        4.54071 |
| student_id_S5298 |        3.7873  |
| student_id_S53   |       -5.41628 |

---

### Blocco 409 (Feature 4081 - 4090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S530  |       13.1472  |
| student_id_S5300 |       12.4131  |
| student_id_S5301 |        7.80755 |
| student_id_S5302 |        1.47744 |
| student_id_S5303 |       -3.19466 |
| student_id_S5305 |       -1.02907 |
| student_id_S5306 |        8.7877  |
| student_id_S5307 |       -6.3135  |
| student_id_S5308 |       -4.53117 |
| student_id_S5309 |       -9.13949 |

---

### Blocco 410 (Feature 4091 - 4100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S531  |    -2.65138    |
| student_id_S5310 |     6.84052    |
| student_id_S5311 |     8.53343    |
| student_id_S5313 |    -1.82521    |
| student_id_S5314 |     1.04539    |
| student_id_S5315 |    13.6805     |
| student_id_S5316 |    13.4989     |
| student_id_S5317 |    -0.00245737 |
| student_id_S5318 |    -9.02005    |
| student_id_S5319 |     5.07378    |

---

### Blocco 411 (Feature 4101 - 4110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S532  |       11.2931  |
| student_id_S5320 |       -2.43853 |
| student_id_S5321 |       -6.08951 |
| student_id_S5322 |        7.53208 |
| student_id_S5323 |        8.19824 |
| student_id_S5324 |        3.30542 |
| student_id_S5325 |       -1.86469 |
| student_id_S5326 |       -9.62305 |
| student_id_S5327 |      -16.4703  |
| student_id_S5328 |       -5.61817 |

---

### Blocco 412 (Feature 4111 - 4120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5329 |      11.694    |
| student_id_S533  |      11.4364   |
| student_id_S5330 |       5.85466  |
| student_id_S5331 |      -6.24682  |
| student_id_S5332 |       7.98814  |
| student_id_S5333 |      13.3765   |
| student_id_S5334 |       7.23171  |
| student_id_S5335 |       0.697079 |
| student_id_S5336 |      -7.42184  |
| student_id_S5337 |      -5.60148  |

---

### Blocco 413 (Feature 4121 - 4130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5338 |        9.72714 |
| student_id_S5339 |        3.47028 |
| student_id_S534  |       -3.33184 |
| student_id_S5340 |        7.95958 |
| student_id_S5342 |       -4.52175 |
| student_id_S5343 |        3.85684 |
| student_id_S5344 |       -1.95058 |
| student_id_S5345 |        1.54996 |
| student_id_S5347 |       -2.64375 |
| student_id_S5348 |       -4.14387 |

---

### Blocco 414 (Feature 4131 - 4140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5350 |       9.67235  |
| student_id_S5351 |       0.887384 |
| student_id_S5352 |     -10.1743   |
| student_id_S5353 |       7.0865   |
| student_id_S5354 |       1.37918  |
| student_id_S5355 |       5.40026  |
| student_id_S5356 |      -5.00989  |
| student_id_S5357 |       6.68632  |
| student_id_S5358 |       7.76691  |
| student_id_S5359 |      -3.40571  |

---

### Blocco 415 (Feature 4141 - 4150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S536  |      -9.11755  |
| student_id_S5360 |      10.2992   |
| student_id_S5361 |       0.443855 |
| student_id_S5362 |       0.837228 |
| student_id_S5363 |       3.01209  |
| student_id_S5364 |      -4.77201  |
| student_id_S5365 |      -2.14402  |
| student_id_S5366 |       1.58855  |
| student_id_S5367 |      15.006    |
| student_id_S5368 |      15.4755   |

---

### Blocco 416 (Feature 4151 - 4160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5369 |       -4.28263 |
| student_id_S537  |        9.12626 |
| student_id_S5370 |        3.72542 |
| student_id_S5372 |       10.0036  |
| student_id_S5373 |        6.81118 |
| student_id_S5375 |        3.06876 |
| student_id_S5376 |        9.69746 |
| student_id_S5377 |       -9.80128 |
| student_id_S5378 |        6.64994 |
| student_id_S5379 |        5.62009 |

---

### Blocco 417 (Feature 4161 - 4170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5380 |       2.25741  |
| student_id_S5381 |      -5.38207  |
| student_id_S5382 |       2.82061  |
| student_id_S5384 |      -9.24961  |
| student_id_S5386 |      -7.29318  |
| student_id_S5387 |      -6.63839  |
| student_id_S5388 |     -11.4992   |
| student_id_S5389 |       0.591825 |
| student_id_S5390 |       3.9699   |
| student_id_S5392 |      -5.12325  |

---

### Blocco 418 (Feature 4171 - 4180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5393 |      -7.34031  |
| student_id_S5394 |      -0.110079 |
| student_id_S5396 |     -11.2209   |
| student_id_S5397 |       8.96331  |
| student_id_S5398 |      10.9841   |
| student_id_S5399 |      -5.9676   |
| student_id_S54   |       4.27643  |
| student_id_S540  |      -3.37563  |
| student_id_S5400 |       5.93651  |
| student_id_S5401 |      -3.65065  |

---

### Blocco 419 (Feature 4181 - 4190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5402 |     -5.29801   |
| student_id_S5403 |    -15.1734    |
| student_id_S5404 |     11.9463    |
| student_id_S5407 |     -4.07094   |
| student_id_S5408 |     -0.0758285 |
| student_id_S5409 |     10.5921    |
| student_id_S541  |      2.92835   |
| student_id_S5410 |      5.00614   |
| student_id_S5411 |      7.576     |
| student_id_S5412 |      3.53519   |

---

### Blocco 420 (Feature 4191 - 4200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5413 |     4.32781    |
| student_id_S5414 |     3.26148    |
| student_id_S5415 |     1.88116    |
| student_id_S5416 |     1.56053    |
| student_id_S5417 |    -1.3856     |
| student_id_S5418 |    -1.17497    |
| student_id_S5419 |     8.22051    |
| student_id_S542  |     2.26019    |
| student_id_S5420 |     9.69517    |
| student_id_S5421 |     0.00659566 |

---

### Blocco 421 (Feature 4201 - 4210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5422 |      -3.74124  |
| student_id_S5423 |       0.324285 |
| student_id_S5424 |       7.37452  |
| student_id_S5425 |       8.79581  |
| student_id_S5426 |       5.28475  |
| student_id_S5427 |      -4.25328  |
| student_id_S5428 |      -2.38174  |
| student_id_S5429 |      -2.66377  |
| student_id_S543  |      -4.68869  |
| student_id_S5430 |       2.50749  |

---

### Blocco 422 (Feature 4211 - 4220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5431 |      -8.27009  |
| student_id_S5433 |      -0.574804 |
| student_id_S5436 |      -4.58991  |
| student_id_S5438 |      -8.54389  |
| student_id_S5439 |     -10.3644   |
| student_id_S544  |       3.56857  |
| student_id_S5440 |       1.21515  |
| student_id_S5441 |       3.14132  |
| student_id_S5443 |      -8.29701  |
| student_id_S5444 |      -1.83527  |

---

### Blocco 423 (Feature 4221 - 4230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5445 |       4.13637  |
| student_id_S5446 |       7.00328  |
| student_id_S5447 |      -2.9805   |
| student_id_S5448 |       0.168733 |
| student_id_S5449 |      -2.47307  |
| student_id_S545  |      -1.51667  |
| student_id_S5450 |      -0.211628 |
| student_id_S5451 |       9.25319  |
| student_id_S5452 |       2.42077  |
| student_id_S5453 |       4.85596  |

---

### Blocco 424 (Feature 4231 - 4240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5454 |        7.59745 |
| student_id_S5457 |        9.85085 |
| student_id_S5459 |        4.21073 |
| student_id_S5460 |        1.93819 |
| student_id_S5462 |        5.79927 |
| student_id_S5463 |       13.5134  |
| student_id_S5464 |       -1.00452 |
| student_id_S5465 |        1.72516 |
| student_id_S5466 |        3.13282 |
| student_id_S5467 |        3.48075 |

---

### Blocco 425 (Feature 4241 - 4250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5468 |      10.287    |
| student_id_S5469 |       7.49908  |
| student_id_S5470 |       3.36754  |
| student_id_S5472 |       0.821433 |
| student_id_S5473 |      14.1895   |
| student_id_S5474 |      11.1714   |
| student_id_S5475 |       8.4465   |
| student_id_S5476 |       7.15476  |
| student_id_S5477 |      -6.28078  |
| student_id_S5478 |      -3.91301  |

---

### Blocco 426 (Feature 4251 - 4260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5480 |     -11.5511   |
| student_id_S5481 |       8.56654  |
| student_id_S5482 |       9.60826  |
| student_id_S5483 |       0.353468 |
| student_id_S5484 |      -3.97066  |
| student_id_S5485 |      -7.67631  |
| student_id_S5486 |      -6.42957  |
| student_id_S5487 |       3.01408  |
| student_id_S5488 |       5.92742  |
| student_id_S5489 |      -1.5091   |

---

### Blocco 427 (Feature 4261 - 4270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5490 |      -1.26998  |
| student_id_S5492 |      -6.17231  |
| student_id_S5493 |      13.5167   |
| student_id_S5494 |      -6.68147  |
| student_id_S5495 |      -1.21617  |
| student_id_S5497 |       0.249089 |
| student_id_S5499 |       2.18846  |
| student_id_S55   |      -0.349988 |
| student_id_S5500 |      -3.65263  |
| student_id_S5501 |       0.218758 |

---

### Blocco 428 (Feature 4271 - 4280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5502 |       5.00228  |
| student_id_S5503 |       3.6513   |
| student_id_S5504 |      -5.13565  |
| student_id_S5506 |       7.05411  |
| student_id_S5507 |       1.8649   |
| student_id_S5508 |       6.86589  |
| student_id_S5509 |      -9.87203  |
| student_id_S5510 |      -0.671637 |
| student_id_S5511 |      -0.877658 |
| student_id_S5512 |       4.33981  |

---

### Blocco 429 (Feature 4281 - 4290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5513 |     -12.5053   |
| student_id_S5515 |      -0.354609 |
| student_id_S5516 |      11.4353   |
| student_id_S5517 |      11.4775   |
| student_id_S5518 |      -7.79341  |
| student_id_S5519 |       0.902805 |
| student_id_S552  |       5.49876  |
| student_id_S5520 |      -6.11028  |
| student_id_S5521 |      -7.73992  |
| student_id_S5522 |      13.8125   |

---

### Blocco 430 (Feature 4291 - 4300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5523 |       5.37994  |
| student_id_S5524 |       5.88689  |
| student_id_S5525 |      11.9994   |
| student_id_S5526 |      -4.50132  |
| student_id_S5528 |      17.5042   |
| student_id_S5529 |      -0.687843 |
| student_id_S553  |      -2.41608  |
| student_id_S5530 |       7.87144  |
| student_id_S5531 |      -2.50495  |
| student_id_S5532 |      -3.18579  |

---

### Blocco 431 (Feature 4301 - 4310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5533 |       1.34964  |
| student_id_S5534 |       3.44966  |
| student_id_S5535 |       0.723933 |
| student_id_S5536 |      -2.23527  |
| student_id_S5537 |      -8.16895  |
| student_id_S5538 |      -6.50512  |
| student_id_S5540 |      -0.689014 |
| student_id_S5541 |      14.5331   |
| student_id_S5543 |      -4.15601  |
| student_id_S5544 |     -11.3967   |

---

### Blocco 432 (Feature 4311 - 4320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5545 |       14.3012  |
| student_id_S5546 |       -5.50028 |
| student_id_S5547 |       -3.45304 |
| student_id_S5548 |        8.21601 |
| student_id_S5549 |        3.19118 |
| student_id_S555  |       -3.27188 |
| student_id_S5550 |       -3.69332 |
| student_id_S5551 |        2.85113 |
| student_id_S5552 |       -1.71348 |
| student_id_S5553 |        6.67457 |

---

### Blocco 433 (Feature 4321 - 4330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5554 |       11.2377  |
| student_id_S5555 |        2.15105 |
| student_id_S5556 |        2.61069 |
| student_id_S5557 |        2.90401 |
| student_id_S5558 |       17.0958  |
| student_id_S556  |        2.54106 |
| student_id_S5560 |       -8.07935 |
| student_id_S5562 |       -6.90981 |
| student_id_S5563 |       -6.95338 |
| student_id_S5565 |      -18.0345  |

---

### Blocco 434 (Feature 4331 - 4340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5567 |       6.32338  |
| student_id_S5568 |       7.7594   |
| student_id_S5569 |       1.16009  |
| student_id_S557  |       0.134374 |
| student_id_S5572 |      10.1045   |
| student_id_S5574 |       6.83821  |
| student_id_S5575 |      -6.49102  |
| student_id_S5576 |       8.12083  |
| student_id_S5577 |      -6.14136  |
| student_id_S5578 |       2.83249  |

---

### Blocco 435 (Feature 4341 - 4350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5579 |       0.540119 |
| student_id_S558  |       9.12994  |
| student_id_S5580 |     -10.3465   |
| student_id_S5583 |       8.49811  |
| student_id_S5584 |      -6.68892  |
| student_id_S5585 |      10.9507   |
| student_id_S5586 |      -7.04153  |
| student_id_S5587 |       3.1711   |
| student_id_S5588 |      -0.499521 |
| student_id_S5589 |       2.99676  |

---

### Blocco 436 (Feature 4351 - 4360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S559  |      -14.4182  |
| student_id_S5590 |       -3.61255 |
| student_id_S5591 |       -5.19916 |
| student_id_S5592 |       -2.06039 |
| student_id_S5594 |       12.0053  |
| student_id_S5595 |       -9.75391 |
| student_id_S5596 |      -11.0665  |
| student_id_S5597 |       18.6597  |
| student_id_S5598 |       -1.95384 |
| student_id_S5600 |        3.07701 |

---

### Blocco 437 (Feature 4361 - 4370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5601 |        0.80669 |
| student_id_S5602 |        2.81407 |
| student_id_S5603 |       15.8558  |
| student_id_S5604 |       14.8393  |
| student_id_S5605 |        2.24269 |
| student_id_S5606 |        0.5839  |
| student_id_S5607 |       -5.71304 |
| student_id_S5608 |      -12.0915  |
| student_id_S5609 |       -6.86771 |
| student_id_S561  |        3.10691 |

---

### Blocco 438 (Feature 4371 - 4380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5612 |       10.2085  |
| student_id_S5615 |       -6.54869 |
| student_id_S5616 |       -0.6946  |
| student_id_S5617 |       -5.79003 |
| student_id_S5618 |       -6.48766 |
| student_id_S5619 |       -3.76174 |
| student_id_S562  |       -2.16542 |
| student_id_S5620 |       -7.37517 |
| student_id_S5621 |        9.5347  |
| student_id_S5622 |        6.93097 |

---

### Blocco 439 (Feature 4381 - 4390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5623 |      -6.47147  |
| student_id_S5624 |      -0.990202 |
| student_id_S5625 |      -3.56441  |
| student_id_S5626 |      15.3201   |
| student_id_S5627 |       5.34985  |
| student_id_S5628 |       5.40073  |
| student_id_S5629 |      -6.52158  |
| student_id_S563  |       6.83491  |
| student_id_S5630 |       6.47491  |
| student_id_S5631 |      -8.8567   |

---

### Blocco 440 (Feature 4391 - 4400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5632 |       9.16638  |
| student_id_S5633 |       4.01873  |
| student_id_S5634 |       8.75712  |
| student_id_S5635 |      -5.23269  |
| student_id_S5636 |       4.44228  |
| student_id_S5637 |       7.3724   |
| student_id_S5638 |      -7.75803  |
| student_id_S5639 |      14.294    |
| student_id_S564  |      -0.112904 |
| student_id_S5640 |       3.94038  |

---

### Blocco 441 (Feature 4401 - 4410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5641 |        5.79086 |
| student_id_S5642 |       -1.84854 |
| student_id_S5643 |        3.21137 |
| student_id_S5644 |       -7.47853 |
| student_id_S5646 |        6.76867 |
| student_id_S5647 |        9.85352 |
| student_id_S5648 |      -16.303   |
| student_id_S5649 |        5.17035 |
| student_id_S565  |        2.51527 |
| student_id_S5650 |        1.6001  |

---

### Blocco 442 (Feature 4411 - 4420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5651 |     11.4056    |
| student_id_S5652 |      2.69093   |
| student_id_S5653 |      8.90449   |
| student_id_S5655 |      0.759721  |
| student_id_S5656 |     13.5169    |
| student_id_S5657 |      2.21814   |
| student_id_S5658 |      5.34878   |
| student_id_S5659 |      1.15511   |
| student_id_S566  |      2.21578   |
| student_id_S5660 |      0.0630693 |

---

### Blocco 443 (Feature 4421 - 4430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5661 |      -3.38695  |
| student_id_S5663 |      -4.93895  |
| student_id_S5664 |       4.60883  |
| student_id_S5665 |      -1.06534  |
| student_id_S5666 |       0.213306 |
| student_id_S5667 |      -0.328561 |
| student_id_S567  |      13.0516   |
| student_id_S5671 |      -2.93686  |
| student_id_S5673 |       5.01777  |
| student_id_S5675 |      13.0486   |

---

### Blocco 444 (Feature 4431 - 4440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5676 |       -1.4541  |
| student_id_S5678 |        9.61754 |
| student_id_S5679 |       12.0564  |
| student_id_S568  |       -2.25504 |
| student_id_S5681 |       -6.96906 |
| student_id_S5682 |        3.11961 |
| student_id_S5684 |       10.4122  |
| student_id_S5685 |        2.16987 |
| student_id_S5687 |       -6.41011 |
| student_id_S5688 |        1.95987 |

---

### Blocco 445 (Feature 4441 - 4450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5689 |       -3.1806  |
| student_id_S569  |       -6.17448 |
| student_id_S5690 |        7.54079 |
| student_id_S5691 |       -5.16963 |
| student_id_S5692 |      -12.6704  |
| student_id_S5693 |      -12.4292  |
| student_id_S5694 |        6.46964 |
| student_id_S5695 |        7.5144  |
| student_id_S5696 |        2.55505 |
| student_id_S5698 |        5.88536 |

---

### Blocco 446 (Feature 4451 - 4460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S57   |      -0.321992 |
| student_id_S570  |       8.42666  |
| student_id_S5700 |       5.17484  |
| student_id_S5701 |       7.38044  |
| student_id_S5702 |      -9.72387  |
| student_id_S5703 |       5.88917  |
| student_id_S5704 |      -3.96998  |
| student_id_S5705 |       4.51725  |
| student_id_S5706 |       5.96592  |
| student_id_S5707 |     -13.7392   |

---

### Blocco 447 (Feature 4461 - 4470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5709 |      -6.77879  |
| student_id_S571  |      -1.52695  |
| student_id_S5710 |      -1.06299  |
| student_id_S5712 |      -5.36206  |
| student_id_S5713 |       0.332578 |
| student_id_S5714 |      14.7766   |
| student_id_S5715 |       4.51537  |
| student_id_S5716 |      -4.17459  |
| student_id_S5717 |      -3.79703  |
| student_id_S5718 |       6.4283   |

---

### Blocco 448 (Feature 4471 - 4480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5719 |       -7.92547 |
| student_id_S572  |       -6.10589 |
| student_id_S5720 |       -3.7097  |
| student_id_S5721 |        5.51292 |
| student_id_S5722 |        7.3328  |
| student_id_S5724 |       12.176   |
| student_id_S5726 |        7.22598 |
| student_id_S5727 |       -2.498   |
| student_id_S5728 |       -8.31014 |
| student_id_S5729 |        8.48134 |

---

### Blocco 449 (Feature 4481 - 4490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S573  |     -2.67832   |
| student_id_S5730 |     13.7116    |
| student_id_S5731 |     -4.8997    |
| student_id_S5732 |     -7.05723   |
| student_id_S5734 |     10.9169    |
| student_id_S5735 |      0.881988  |
| student_id_S5737 |     -0.0576152 |
| student_id_S5738 |     -9.79993   |
| student_id_S5739 |      9.1304    |
| student_id_S574  |     -4.70684   |

---

### Blocco 450 (Feature 4491 - 4500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5740 |     10.6339    |
| student_id_S5742 |     -8.60044   |
| student_id_S5743 |      8.0164    |
| student_id_S5745 |      4.83507   |
| student_id_S5746 |      9.3251    |
| student_id_S5747 |     -0.0665233 |
| student_id_S5748 |    -13.33      |
| student_id_S5749 |     12.7137    |
| student_id_S575  |      0.549822  |
| student_id_S5750 |      8.5045    |

---

### Blocco 451 (Feature 4501 - 4510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5751 |       -6.57771 |
| student_id_S5752 |        4.48787 |
| student_id_S5753 |       10.64    |
| student_id_S5754 |        6.22144 |
| student_id_S5755 |      -14.3965  |
| student_id_S5756 |        4.20899 |
| student_id_S5757 |       -3.5054  |
| student_id_S5760 |       11.6385  |
| student_id_S5761 |       11.4673  |
| student_id_S5763 |       -3.94905 |

---

### Blocco 452 (Feature 4511 - 4520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5764 |        8.69771 |
| student_id_S5766 |       -4.48887 |
| student_id_S5767 |       -4.57107 |
| student_id_S5768 |       -1.86798 |
| student_id_S5769 |       -7.16965 |
| student_id_S577  |       -7.96364 |
| student_id_S5770 |        8.98538 |
| student_id_S5771 |       13.4599  |
| student_id_S5772 |       -2.47264 |
| student_id_S5773 |       -6.63807 |

---

### Blocco 453 (Feature 4521 - 4530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5774 |      -6.16003  |
| student_id_S5776 |      -1.74264  |
| student_id_S5778 |       4.59083  |
| student_id_S5779 |      -3.79061  |
| student_id_S578  |       0.704001 |
| student_id_S5780 |       6.6785   |
| student_id_S5781 |       6.96908  |
| student_id_S5783 |      -6.75048  |
| student_id_S5784 |       1.6206   |
| student_id_S5785 |     -14.5376   |

---

### Blocco 454 (Feature 4531 - 4540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5786 |       -2.5132  |
| student_id_S5787 |        2.26245 |
| student_id_S5788 |       -2.73665 |
| student_id_S5789 |      -10.7029  |
| student_id_S579  |      -10.8821  |
| student_id_S5791 |       -7.02065 |
| student_id_S5793 |       -4.79576 |
| student_id_S5794 |        3.93327 |
| student_id_S5795 |       -7.54878 |
| student_id_S5796 |        1.24415 |

---

### Blocco 455 (Feature 4541 - 4550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5797 |      -9.45562  |
| student_id_S5798 |       7.50355  |
| student_id_S5799 |       7.82048  |
| student_id_S58   |      -6.87559  |
| student_id_S580  |      -3.09296  |
| student_id_S5800 |       2.74162  |
| student_id_S5801 |       1.63798  |
| student_id_S5802 |       1.13616  |
| student_id_S5803 |      -5.25784  |
| student_id_S5804 |       0.916268 |

---

### Blocco 456 (Feature 4551 - 4560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5805 |      -9.95466  |
| student_id_S5806 |       7.56357  |
| student_id_S5809 |      -4.13303  |
| student_id_S581  |       0.42951  |
| student_id_S5810 |     -10.253    |
| student_id_S5811 |      -2.83171  |
| student_id_S5812 |       7.69672  |
| student_id_S5813 |      -9.52712  |
| student_id_S5814 |      -6.96765  |
| student_id_S5815 |       0.662206 |

---

### Blocco 457 (Feature 4561 - 4570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5816 |      -10.0911  |
| student_id_S5817 |        6.56468 |
| student_id_S5818 |        1.09111 |
| student_id_S582  |       -3.31651 |
| student_id_S5820 |        7.96465 |
| student_id_S5821 |       -1.80229 |
| student_id_S5822 |       -1.8553  |
| student_id_S5823 |      -11.5357  |
| student_id_S5826 |       12.1225  |
| student_id_S5827 |        7.41122 |

---

### Blocco 458 (Feature 4571 - 4580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5828 |       0.642126 |
| student_id_S5829 |       6.61708  |
| student_id_S583  |      -2.49151  |
| student_id_S5830 |      -3.25274  |
| student_id_S5831 |       8.75921  |
| student_id_S5833 |      -4.88622  |
| student_id_S5834 |       5.8882   |
| student_id_S5836 |      -3.38513  |
| student_id_S5837 |      16.4645   |
| student_id_S5838 |       2.50571  |

---

### Blocco 459 (Feature 4581 - 4590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S584  |       2.58802  |
| student_id_S5840 |       9.7581   |
| student_id_S5841 |       7.01851  |
| student_id_S5842 |       1.84385  |
| student_id_S5843 |     -13.3153   |
| student_id_S5845 |      -0.866045 |
| student_id_S5846 |      -2.13123  |
| student_id_S5847 |      -5.87154  |
| student_id_S5849 |      -4.33111  |
| student_id_S585  |       6.80829  |

---

### Blocco 460 (Feature 4591 - 4600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5850 |      -0.741101 |
| student_id_S5851 |       9.5864   |
| student_id_S5852 |       3.37438  |
| student_id_S5853 |      10.4617   |
| student_id_S5854 |      -7.57107  |
| student_id_S5855 |      -6.75214  |
| student_id_S5857 |       2.65682  |
| student_id_S5858 |       0.633375 |
| student_id_S5859 |       2.65178  |
| student_id_S586  |       4.64547  |

---

### Blocco 461 (Feature 4601 - 4610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5860 |        1.86621 |
| student_id_S5861 |       13.6465  |
| student_id_S5862 |       10.8319  |
| student_id_S5863 |        2.90127 |
| student_id_S5864 |      -10.6684  |
| student_id_S5865 |       10.2855  |
| student_id_S5866 |       12.1805  |
| student_id_S5868 |        4.10079 |
| student_id_S5869 |       -2.84479 |
| student_id_S5870 |       -2.09198 |

---

### Blocco 462 (Feature 4611 - 4620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5871 |       11.7781  |
| student_id_S5873 |        7.95632 |
| student_id_S5874 |        7.65138 |
| student_id_S5875 |       10.9196  |
| student_id_S5876 |       11.8561  |
| student_id_S5877 |       -2.15545 |
| student_id_S5878 |        6.24212 |
| student_id_S5879 |      -13.9102  |
| student_id_S588  |       -1.3872  |
| student_id_S5880 |        2.24523 |

---

### Blocco 463 (Feature 4621 - 4630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5881 |        3.56643 |
| student_id_S5882 |       -2.25287 |
| student_id_S5883 |       -1.07328 |
| student_id_S5884 |       -9.46626 |
| student_id_S5885 |       -9.63194 |
| student_id_S5886 |       11.7495  |
| student_id_S5887 |      -10.9015  |
| student_id_S5888 |       -1.2431  |
| student_id_S5889 |        5.28645 |
| student_id_S5891 |        9.12533 |

---

### Blocco 464 (Feature 4631 - 4640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5892 |      -1.1585   |
| student_id_S5893 |       3.01521  |
| student_id_S5894 |      -7.53592  |
| student_id_S5895 |      -8.33408  |
| student_id_S5896 |       9.75083  |
| student_id_S5897 |      -2.49413  |
| student_id_S5898 |      12.3529   |
| student_id_S5899 |      -0.962275 |
| student_id_S590  |      11.1507   |
| student_id_S5900 |       5.26784  |

---

### Blocco 465 (Feature 4641 - 4650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5901 |        2.32301 |
| student_id_S5902 |        0.52337 |
| student_id_S5904 |        7.09471 |
| student_id_S5905 |       10.466   |
| student_id_S5906 |       -9.64088 |
| student_id_S5907 |       -9.93674 |
| student_id_S5908 |       14.1469  |
| student_id_S591  |       -8.59874 |
| student_id_S5910 |        5.54262 |
| student_id_S5911 |        1.40572 |

---

### Blocco 466 (Feature 4651 - 4660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5912 |       8.32649  |
| student_id_S5913 |      -3.22328  |
| student_id_S5914 |      -1.60365  |
| student_id_S5915 |       9.12555  |
| student_id_S5917 |      10.9142   |
| student_id_S5918 |       0.395681 |
| student_id_S5919 |     -11.5916   |
| student_id_S592  |       4.09889  |
| student_id_S5921 |      -7.3732   |
| student_id_S5922 |       0.885349 |

---

### Blocco 467 (Feature 4661 - 4670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5924 |      -6.21356  |
| student_id_S5925 |      -3.38102  |
| student_id_S5927 |       2.18141  |
| student_id_S5928 |       7.42389  |
| student_id_S5929 |      11.2283   |
| student_id_S593  |      14.0449   |
| student_id_S5930 |      -0.466282 |
| student_id_S5931 |       3.95787  |
| student_id_S5932 |       9.2797   |
| student_id_S5933 |      -4.24388  |

---

### Blocco 468 (Feature 4671 - 4680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5934 |      -10.9859  |
| student_id_S5935 |       -8.72172 |
| student_id_S5936 |       -6.77468 |
| student_id_S5937 |        4.99949 |
| student_id_S5938 |        4.34727 |
| student_id_S5941 |       -7.99456 |
| student_id_S5942 |      -15.2806  |
| student_id_S5943 |       -5.59933 |
| student_id_S5944 |       -6.09964 |
| student_id_S5945 |       -1.05114 |

---

### Blocco 469 (Feature 4681 - 4690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5946 |       3.93566  |
| student_id_S5947 |       1.7885   |
| student_id_S5948 |       0.91685  |
| student_id_S5949 |       2.26826  |
| student_id_S595  |      -6.16537  |
| student_id_S5950 |      -0.240475 |
| student_id_S5951 |       6.88831  |
| student_id_S5952 |      11.3994   |
| student_id_S5953 |      13.7195   |
| student_id_S5954 |      -4.15073  |

---

### Blocco 470 (Feature 4691 - 4700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5955 |       4.90625  |
| student_id_S5956 |       2.46897  |
| student_id_S5957 |     -10.6539   |
| student_id_S5959 |       1.06957  |
| student_id_S596  |      -8.53319  |
| student_id_S5960 |       0.641827 |
| student_id_S5961 |      -1.45154  |
| student_id_S5962 |      -1.89557  |
| student_id_S5963 |      -7.04448  |
| student_id_S5964 |       2.31801  |

---

### Blocco 471 (Feature 4701 - 4710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5966 |       13.7674  |
| student_id_S5967 |        2.7483  |
| student_id_S5968 |       -2.52303 |
| student_id_S5969 |        1.86472 |
| student_id_S597  |       -1.96899 |
| student_id_S5970 |       -2.26963 |
| student_id_S5972 |        5.34386 |
| student_id_S5973 |        9.30386 |
| student_id_S5974 |        7.99211 |
| student_id_S5975 |        8.41621 |

---

### Blocco 472 (Feature 4711 - 4720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5978 |      -8.67689  |
| student_id_S598  |       2.98142  |
| student_id_S5980 |       2.04504  |
| student_id_S5981 |      11.9702   |
| student_id_S5982 |       6.9131   |
| student_id_S5983 |       0.208187 |
| student_id_S5984 |       3.7113   |
| student_id_S5985 |      -1.16305  |
| student_id_S5986 |       8.36776  |
| student_id_S5987 |       4.0307   |

---

### Blocco 473 (Feature 4721 - 4730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5988 |       -1.28328 |
| student_id_S5989 |       -7.32804 |
| student_id_S5990 |       -5.17026 |
| student_id_S5991 |        8.83733 |
| student_id_S5992 |       -6.32135 |
| student_id_S5993 |       14.4662  |
| student_id_S5994 |        3.78971 |
| student_id_S5996 |       -5.08204 |
| student_id_S5997 |        3.89599 |
| student_id_S5998 |        1.12715 |

---

### Blocco 474 (Feature 4731 - 4740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S5999 |        9.01658 |
| student_id_S60   |        1.00334 |
| student_id_S600  |        7.39872 |
| student_id_S6000 |        1.82629 |
| student_id_S6001 |        9.55435 |
| student_id_S6002 |       -6.90895 |
| student_id_S6003 |        7.42743 |
| student_id_S6004 |       -7.75547 |
| student_id_S6005 |        2.80459 |
| student_id_S6006 |       10.5185  |

---

### Blocco 475 (Feature 4741 - 4750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6007 |       -4.23521 |
| student_id_S6008 |        7.88828 |
| student_id_S6009 |        8.55171 |
| student_id_S601  |        5.97334 |
| student_id_S6010 |        7.73909 |
| student_id_S6011 |        5.52275 |
| student_id_S6012 |       -9.28074 |
| student_id_S6013 |       -4.43049 |
| student_id_S6014 |        8.32282 |
| student_id_S6015 |        1.50169 |

---

### Blocco 476 (Feature 4751 - 4760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6016 |        2.61404 |
| student_id_S6017 |       -4.36709 |
| student_id_S6018 |       -6.00432 |
| student_id_S6019 |        7.73951 |
| student_id_S602  |       -4.16639 |
| student_id_S6020 |       -3.33526 |
| student_id_S6021 |       -4.2967  |
| student_id_S6022 |       -0.28547 |
| student_id_S6023 |        8.6065  |
| student_id_S6024 |       -8.27295 |

---

### Blocco 477 (Feature 4761 - 4770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6025 |        3.42554 |
| student_id_S6026 |       -1.49127 |
| student_id_S6027 |       -1.09796 |
| student_id_S6028 |       10.7519  |
| student_id_S603  |       -2.47894 |
| student_id_S6030 |       -5.1233  |
| student_id_S6031 |        3.70737 |
| student_id_S6034 |       -5.14044 |
| student_id_S6035 |      -10.1085  |
| student_id_S6036 |       -4.23391 |

---

### Blocco 478 (Feature 4771 - 4780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6038 |       -2.21449 |
| student_id_S6039 |       -7.34261 |
| student_id_S604  |       -1.86298 |
| student_id_S6040 |        8.03854 |
| student_id_S6041 |       -4.58348 |
| student_id_S6042 |        6.85995 |
| student_id_S6043 |        1.6578  |
| student_id_S6044 |        7.28682 |
| student_id_S6048 |       12.689   |
| student_id_S6049 |       -2.49417 |

---

### Blocco 479 (Feature 4781 - 4790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S605  |       -9.64646 |
| student_id_S6050 |       10.4186  |
| student_id_S6051 |       -4.33999 |
| student_id_S6052 |      -11.5432  |
| student_id_S6053 |        4.25234 |
| student_id_S6054 |        3.22551 |
| student_id_S6055 |       -4.02267 |
| student_id_S6056 |       15.5022  |
| student_id_S6058 |       -4.07811 |
| student_id_S6059 |       -7.97856 |

---

### Blocco 480 (Feature 4791 - 4800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S606  |        2.23958 |
| student_id_S6060 |       -0.60347 |
| student_id_S6061 |       -3.88853 |
| student_id_S6062 |       -4.27152 |
| student_id_S6063 |       -7.49648 |
| student_id_S6064 |       -9.08488 |
| student_id_S6066 |       -9.90188 |
| student_id_S6067 |        6.07026 |
| student_id_S6068 |        8.0074  |
| student_id_S607  |      -10.9208  |

---

### Blocco 481 (Feature 4801 - 4810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6070 |        3.2848  |
| student_id_S6071 |       -2.84771 |
| student_id_S6072 |        8.07361 |
| student_id_S6073 |      -12.77    |
| student_id_S6074 |       -1.96679 |
| student_id_S6075 |       -9.48699 |
| student_id_S6076 |       -2.20941 |
| student_id_S6077 |        5.74369 |
| student_id_S6078 |       13.1897  |
| student_id_S6079 |       -7.45447 |

---

### Blocco 482 (Feature 4811 - 4820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S608  |       -6.22615 |
| student_id_S6080 |       10.1102  |
| student_id_S6081 |       13.0225  |
| student_id_S6082 |        1.34809 |
| student_id_S6083 |        1.90799 |
| student_id_S6084 |       -3.5072  |
| student_id_S6086 |        3.67485 |
| student_id_S6087 |       12.8264  |
| student_id_S6088 |       -5.03463 |
| student_id_S6089 |        2.95922 |

---

### Blocco 483 (Feature 4821 - 4830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S609  |       -3.66614 |
| student_id_S6090 |       10.4326  |
| student_id_S6092 |        5.50072 |
| student_id_S6093 |       -1.18534 |
| student_id_S6094 |       -2.18019 |
| student_id_S6095 |        4.32789 |
| student_id_S6096 |       14.2444  |
| student_id_S6099 |       -2.69116 |
| student_id_S61   |       10.4344  |
| student_id_S610  |        2.47184 |

---

### Blocco 484 (Feature 4831 - 4840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6100 |        2.8283  |
| student_id_S6101 |       -4.68866 |
| student_id_S6102 |        9.81696 |
| student_id_S6103 |       -4.53248 |
| student_id_S6104 |        1.15096 |
| student_id_S6105 |        1.6388  |
| student_id_S6106 |       -3.05107 |
| student_id_S6107 |      -12.6714  |
| student_id_S6108 |       -4.30275 |
| student_id_S611  |        9.8432  |

---

### Blocco 485 (Feature 4841 - 4850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6111 |      -4.44821  |
| student_id_S6112 |      -2.37082  |
| student_id_S6113 |       9.43075  |
| student_id_S6114 |       1.68131  |
| student_id_S6116 |      -1.78573  |
| student_id_S6117 |      -0.111161 |
| student_id_S6118 |       6.89095  |
| student_id_S6119 |      -0.778031 |
| student_id_S612  |       2.25608  |
| student_id_S6121 |      -4.38579  |

---

### Blocco 486 (Feature 4851 - 4860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6122 |       11.201   |
| student_id_S6123 |        3.00269 |
| student_id_S6125 |        2.3766  |
| student_id_S6126 |        1.83512 |
| student_id_S6127 |       -3.22949 |
| student_id_S6128 |       -1.51702 |
| student_id_S6129 |        8.77765 |
| student_id_S6130 |        5.18784 |
| student_id_S6131 |       -1.47127 |
| student_id_S6132 |        1.44394 |

---

### Blocco 487 (Feature 4861 - 4870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6133 |        8.20494 |
| student_id_S6134 |       -4.19832 |
| student_id_S6135 |      -12.6324  |
| student_id_S6136 |        9.39194 |
| student_id_S6137 |        3.37296 |
| student_id_S6138 |       -9.99361 |
| student_id_S6139 |       10.8208  |
| student_id_S614  |        1.12832 |
| student_id_S6140 |       -5.44661 |
| student_id_S6141 |        1.45666 |

---

### Blocco 488 (Feature 4871 - 4880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6142 |       3.37265  |
| student_id_S6143 |      -3.55621  |
| student_id_S6144 |      -1.55042  |
| student_id_S6145 |       3.96326  |
| student_id_S6146 |      -3.39863  |
| student_id_S6147 |       0.771537 |
| student_id_S6148 |      -5.73297  |
| student_id_S6149 |       8.2459   |
| student_id_S615  |      -6.94479  |
| student_id_S6150 |      -1.79864  |

---

### Blocco 489 (Feature 4881 - 4890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6151 |      6.33044   |
| student_id_S6152 |      1.47571   |
| student_id_S6153 |      6.96723   |
| student_id_S6155 |      0.756943  |
| student_id_S6156 |      4.83137   |
| student_id_S6157 |      5.94678   |
| student_id_S6158 |     -0.0647724 |
| student_id_S616  |      8.64111   |
| student_id_S6160 |      3.00236   |
| student_id_S6162 |      2.93326   |

---

### Blocco 490 (Feature 4891 - 4900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6163 |       -4.08468 |
| student_id_S6165 |        1.75263 |
| student_id_S6166 |       -7.60293 |
| student_id_S6167 |      -10.5002  |
| student_id_S6168 |        7.24602 |
| student_id_S6169 |        1.6416  |
| student_id_S617  |       -5.20006 |
| student_id_S6170 |      -10.2719  |
| student_id_S6172 |       -2.58785 |
| student_id_S6173 |        2.33755 |

---

### Blocco 491 (Feature 4901 - 4910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6174 |       -6.67965 |
| student_id_S6175 |        3.74644 |
| student_id_S6176 |       10.0479  |
| student_id_S6177 |       -3.84124 |
| student_id_S6178 |        3.83693 |
| student_id_S6179 |        8.95341 |
| student_id_S618  |        2.45274 |
| student_id_S6180 |       13.6301  |
| student_id_S6181 |        3.01188 |
| student_id_S6182 |       -8.33665 |

---

### Blocco 492 (Feature 4911 - 4920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6183 |     -10.3546   |
| student_id_S6184 |       1.96676  |
| student_id_S6185 |       3.14843  |
| student_id_S6186 |      -0.353884 |
| student_id_S6188 |       5.74511  |
| student_id_S6189 |       0.370054 |
| student_id_S619  |      -4.85324  |
| student_id_S6190 |       5.18282  |
| student_id_S6192 |       0.385076 |
| student_id_S6193 |      -3.61188  |

---

### Blocco 493 (Feature 4921 - 4930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6194 |      -2.58789  |
| student_id_S6197 |      13.7319   |
| student_id_S6199 |       8.31113  |
| student_id_S62   |      -0.751291 |
| student_id_S620  |       7.66636  |
| student_id_S6201 |      11.5259   |
| student_id_S6203 |       6.49826  |
| student_id_S6205 |       3.11386  |
| student_id_S6206 |       5.02715  |
| student_id_S6207 |       8.87278  |

---

### Blocco 494 (Feature 4931 - 4940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6208 |       -1.25359 |
| student_id_S6209 |       -5.48289 |
| student_id_S621  |       -5.76697 |
| student_id_S6212 |        8.7757  |
| student_id_S6213 |       -5.71627 |
| student_id_S6214 |        3.04625 |
| student_id_S6215 |        2.23026 |
| student_id_S6216 |        6.49946 |
| student_id_S6218 |      -14.009   |
| student_id_S6219 |        9.35081 |

---

### Blocco 495 (Feature 4941 - 4950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S622  |      2.24069   |
| student_id_S6220 |      2.69184   |
| student_id_S6221 |      2.85057   |
| student_id_S6222 |     -5.56911   |
| student_id_S6224 |      5.44505   |
| student_id_S6225 |      4.55266   |
| student_id_S6226 |     -9.73863   |
| student_id_S6227 |     -0.0142295 |
| student_id_S6228 |     -2.85181   |
| student_id_S6229 |     -2.61708   |

---

### Blocco 496 (Feature 4951 - 4960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S623  |        2.7737  |
| student_id_S6230 |        9.76818 |
| student_id_S6231 |       13.2838  |
| student_id_S6232 |       10.788   |
| student_id_S6233 |        8.53545 |
| student_id_S6235 |        6.37451 |
| student_id_S6236 |        6.6529  |
| student_id_S6237 |        4.00485 |
| student_id_S6238 |        5.87532 |
| student_id_S6239 |       -3.83266 |

---

### Blocco 497 (Feature 4961 - 4970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S624  |       4.39228  |
| student_id_S6240 |      -6.79736  |
| student_id_S6241 |       0.99359  |
| student_id_S6243 |      -5.53328  |
| student_id_S6244 |      -6.326    |
| student_id_S6245 |      -7.10484  |
| student_id_S6246 |       0.587202 |
| student_id_S6247 |       5.05702  |
| student_id_S6248 |      -1.59225  |
| student_id_S6249 |      10.9799   |

---

### Blocco 498 (Feature 4971 - 4980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S625  |       2.90045  |
| student_id_S6250 |       0.90421  |
| student_id_S6251 |      -5.59413  |
| student_id_S6253 |      -1.2916   |
| student_id_S6254 |     -13.957    |
| student_id_S6255 |      -8.63392  |
| student_id_S6257 |      -6.48171  |
| student_id_S6258 |      -0.532395 |
| student_id_S626  |      -2.9563   |
| student_id_S6260 |      -4.22214  |

---

### Blocco 499 (Feature 4981 - 4990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6261 |       0.211836 |
| student_id_S6262 |       4.67392  |
| student_id_S6264 |       2.92374  |
| student_id_S6266 |      -1.56623  |
| student_id_S6267 |      11.3886   |
| student_id_S6268 |     -11.4161   |
| student_id_S6269 |       0.049929 |
| student_id_S627  |       3.07851  |
| student_id_S6270 |      19.1058   |
| student_id_S6271 |       5.66448  |

---

### Blocco 500 (Feature 4991 - 5000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6272 |        5.21829 |
| student_id_S6273 |       -2.41439 |
| student_id_S6274 |       10.0885  |
| student_id_S6275 |        4.98709 |
| student_id_S6276 |       -9.10315 |
| student_id_S6277 |       14.3643  |
| student_id_S6278 |        8.55248 |
| student_id_S6279 |        2.64742 |
| student_id_S628  |       -7.85659 |
| student_id_S6280 |        5.30736 |

---

### Blocco 501 (Feature 5001 - 5010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6281 |       0.927456 |
| student_id_S6282 |      -0.741968 |
| student_id_S6283 |       9.71182  |
| student_id_S6286 |       0.416739 |
| student_id_S6287 |      -0.076462 |
| student_id_S6288 |      -9.92199  |
| student_id_S6289 |      -3.70901  |
| student_id_S629  |       0.24854  |
| student_id_S6290 |      -7.58101  |
| student_id_S6291 |     -14.391    |

---

### Blocco 502 (Feature 5011 - 5020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6292 |       -5.3504  |
| student_id_S6293 |       -4.06104 |
| student_id_S6294 |       -6.98758 |
| student_id_S6295 |       11.6676  |
| student_id_S6296 |        1.10481 |
| student_id_S6297 |       -8.15236 |
| student_id_S6298 |       10.9363  |
| student_id_S6299 |        6.21259 |
| student_id_S63   |        7.66599 |
| student_id_S630  |      -15.6589  |

---

### Blocco 503 (Feature 5021 - 5030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6300 |     -12.4027   |
| student_id_S6301 |      -8.83219  |
| student_id_S6303 |       2.51058  |
| student_id_S6304 |     -12.7337   |
| student_id_S6305 |      10.726    |
| student_id_S6306 |      -4.77056  |
| student_id_S6307 |     -10.0125   |
| student_id_S6309 |       9.49648  |
| student_id_S631  |      -4.96713  |
| student_id_S6310 |       0.634537 |

---

### Blocco 504 (Feature 5031 - 5040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6311 |       -4.78738 |
| student_id_S6312 |       -8.3078  |
| student_id_S6314 |        9.19344 |
| student_id_S6315 |        5.98514 |
| student_id_S6316 |        2.64345 |
| student_id_S6317 |        2.90844 |
| student_id_S6318 |        6.69531 |
| student_id_S6319 |       -1.49221 |
| student_id_S632  |       10.6101  |
| student_id_S6322 |        9.1343  |

---

### Blocco 505 (Feature 5041 - 5050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6323 |        7.2435  |
| student_id_S6324 |      -11.6045  |
| student_id_S6325 |       -7.46347 |
| student_id_S6326 |        4.74002 |
| student_id_S6328 |        6.97158 |
| student_id_S6329 |        5.36394 |
| student_id_S633  |        6.32842 |
| student_id_S6330 |        3.12745 |
| student_id_S6331 |        3.6653  |
| student_id_S6332 |        2.374   |

---

### Blocco 506 (Feature 5051 - 5060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6334 |     -12.1446   |
| student_id_S6335 |      -2.49214  |
| student_id_S6337 |      -4.31879  |
| student_id_S6338 |      -1.36246  |
| student_id_S6339 |      -4.90624  |
| student_id_S6340 |      -7.63068  |
| student_id_S6341 |      14.6604   |
| student_id_S6343 |       0.77379  |
| student_id_S6345 |      -0.654492 |
| student_id_S6346 |      16.3306   |

---

### Blocco 507 (Feature 5061 - 5070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6347 |     -12.5      |
| student_id_S6348 |      -9.01791  |
| student_id_S6349 |      -4.46728  |
| student_id_S635  |      -0.508539 |
| student_id_S6350 |       4.60626  |
| student_id_S6351 |      10.5863   |
| student_id_S6352 |      -0.173871 |
| student_id_S6353 |       2.79944  |
| student_id_S6354 |      -2.63636  |
| student_id_S6355 |      -2.19332  |

---

### Blocco 508 (Feature 5071 - 5080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6356 |       10.6376  |
| student_id_S6357 |       -1.88146 |
| student_id_S6358 |       -8.62874 |
| student_id_S6359 |       -7.3389  |
| student_id_S636  |       -9.17576 |
| student_id_S6360 |       -3.96476 |
| student_id_S6361 |       13.6284  |
| student_id_S6362 |        5.44621 |
| student_id_S6363 |       -2.90733 |
| student_id_S6364 |       -6.10032 |

---

### Blocco 509 (Feature 5081 - 5090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6366 |      -10.8699  |
| student_id_S6367 |        4.01198 |
| student_id_S6369 |        9.03086 |
| student_id_S637  |        3.04217 |
| student_id_S6370 |       -2.21077 |
| student_id_S6371 |        7.57294 |
| student_id_S6372 |        5.68282 |
| student_id_S6373 |        3.72362 |
| student_id_S6374 |       -7.5767  |
| student_id_S6375 |       -7.22442 |

---

### Blocco 510 (Feature 5091 - 5100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6376 |       0.339799 |
| student_id_S6377 |       4.62832  |
| student_id_S6378 |       3.02071  |
| student_id_S6379 |       4.9155   |
| student_id_S638  |       4.5145   |
| student_id_S6380 |      -0.437625 |
| student_id_S6381 |      -5.77315  |
| student_id_S6382 |       4.21768  |
| student_id_S6383 |      -5.92103  |
| student_id_S6385 |      -6.67305  |

---

### Blocco 511 (Feature 5101 - 5110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6386 |      16.1549   |
| student_id_S6387 |      -6.47779  |
| student_id_S6389 |      14.3531   |
| student_id_S639  |      -0.912964 |
| student_id_S6390 |      -4.17841  |
| student_id_S6391 |       1.38738  |
| student_id_S6392 |       9.55258  |
| student_id_S6393 |       0.946576 |
| student_id_S6394 |      -6.07007  |
| student_id_S6395 |      10.5742   |

---

### Blocco 512 (Feature 5111 - 5120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6396 |      -1.24987  |
| student_id_S6397 |       0.489293 |
| student_id_S6398 |      -2.22021  |
| student_id_S6399 |       2.0734   |
| student_id_S64   |       5.09749  |
| student_id_S640  |      -0.872011 |
| student_id_S6400 |      15.6453   |
| student_id_S6402 |      10.4974   |
| student_id_S6404 |       5.02397  |
| student_id_S6405 |      -0.134752 |

---

### Blocco 513 (Feature 5121 - 5130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6406 |      -4.38285  |
| student_id_S6409 |       6.24094  |
| student_id_S641  |     -11.8924   |
| student_id_S6410 |       0.485662 |
| student_id_S6411 |       0.839285 |
| student_id_S6412 |       9.65697  |
| student_id_S6413 |      -6.98387  |
| student_id_S6414 |     -14.0742   |
| student_id_S6415 |       9.27285  |
| student_id_S6417 |      -4.69649  |

---

### Blocco 514 (Feature 5131 - 5140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6418 |      -14.0973  |
| student_id_S6419 |       -1.13829 |
| student_id_S642  |       13.7875  |
| student_id_S6420 |       -9.32564 |
| student_id_S6421 |       -3.96611 |
| student_id_S6422 |       -3.57656 |
| student_id_S6423 |       -7.44272 |
| student_id_S6424 |       -9.96061 |
| student_id_S6425 |       -4.65917 |
| student_id_S6426 |        6.83875 |

---

### Blocco 515 (Feature 5141 - 5150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6427 |        9.4142  |
| student_id_S6428 |        2.56905 |
| student_id_S6429 |       -2.32401 |
| student_id_S643  |       -3.4729  |
| student_id_S6430 |        8.92377 |
| student_id_S6431 |       -7.66326 |
| student_id_S6432 |       -6.18616 |
| student_id_S6434 |       13.0339  |
| student_id_S6435 |        1.05094 |
| student_id_S6436 |        7.80729 |

---

### Blocco 516 (Feature 5151 - 5160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6437 |       10.1161  |
| student_id_S6438 |        2.8644  |
| student_id_S6439 |        5.54893 |
| student_id_S644  |       -6.34812 |
| student_id_S6440 |      -10.8333  |
| student_id_S6441 |        7.44205 |
| student_id_S6442 |        5.80632 |
| student_id_S6443 |       -2.71278 |
| student_id_S6444 |        5.60422 |
| student_id_S6445 |       -3.16378 |

---

### Blocco 517 (Feature 5161 - 5170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6446 |       4.52874  |
| student_id_S6447 |      -8.49864  |
| student_id_S6448 |      -2.76446  |
| student_id_S645  |       2.12347  |
| student_id_S6450 |       0.140765 |
| student_id_S6453 |      -2.59602  |
| student_id_S6455 |      -3.02282  |
| student_id_S6456 |     -14.7378   |
| student_id_S6457 |       5.5709   |
| student_id_S6458 |      10.8541   |

---

### Blocco 518 (Feature 5171 - 5180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6459 |       -1.73935 |
| student_id_S646  |       -3.04949 |
| student_id_S6460 |        1.45864 |
| student_id_S6461 |        5.26241 |
| student_id_S6462 |      -14.4286  |
| student_id_S6463 |        3.38186 |
| student_id_S6464 |        1.33412 |
| student_id_S6465 |        3.26565 |
| student_id_S6466 |       -6.80945 |
| student_id_S6468 |       -8.77726 |

---

### Blocco 519 (Feature 5181 - 5190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S647  |      -6.50981  |
| student_id_S6470 |      -1.00948  |
| student_id_S6471 |     -10.379    |
| student_id_S6472 |       7.60665  |
| student_id_S6473 |       0.954207 |
| student_id_S6475 |       7.34291  |
| student_id_S6476 |      -5.90604  |
| student_id_S6477 |     -11.0643   |
| student_id_S6478 |       0.520836 |
| student_id_S6479 |      -5.58935  |

---

### Blocco 520 (Feature 5191 - 5200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S648  |        1.73842 |
| student_id_S6481 |       -1.76391 |
| student_id_S6482 |       12.5562  |
| student_id_S6483 |      -10.6773  |
| student_id_S6484 |       -9.15714 |
| student_id_S6485 |        7.12904 |
| student_id_S6486 |        7.69944 |
| student_id_S6488 |       -4.06783 |
| student_id_S6489 |       11.3335  |
| student_id_S6492 |      -10.1821  |

---

### Blocco 521 (Feature 5201 - 5210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6494 |      -14.2569  |
| student_id_S6496 |       -8.53297 |
| student_id_S6497 |        9.96684 |
| student_id_S6498 |       -7.68171 |
| student_id_S6499 |        1.23163 |
| student_id_S65   |       -8.11732 |
| student_id_S650  |        3.86605 |
| student_id_S6500 |        4.56901 |
| student_id_S6501 |       -8.71864 |
| student_id_S6503 |       11.9239  |

---

### Blocco 522 (Feature 5211 - 5220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6504 |        8.21338 |
| student_id_S6506 |        2.22533 |
| student_id_S6507 |       -7.77783 |
| student_id_S6508 |        4.32164 |
| student_id_S6509 |        2.99581 |
| student_id_S651  |       13.2688  |
| student_id_S6511 |       -3.36315 |
| student_id_S6512 |        4.80222 |
| student_id_S6513 |        4.13652 |
| student_id_S6514 |        5.68657 |

---

### Blocco 523 (Feature 5221 - 5230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6515 |      9.34592   |
| student_id_S6516 |     14.0959    |
| student_id_S6517 |     13.2153    |
| student_id_S6518 |     -9.56383   |
| student_id_S6519 |      1.83874   |
| student_id_S652  |     -5.8179    |
| student_id_S6521 |      0.0478121 |
| student_id_S6522 |     -9.00981   |
| student_id_S6523 |     -4.46668   |
| student_id_S6524 |    -11.2686    |

---

### Blocco 524 (Feature 5231 - 5240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6525 |        7.40936 |
| student_id_S6526 |       -2.78162 |
| student_id_S6527 |        3.00708 |
| student_id_S6529 |        1.68116 |
| student_id_S6530 |        3.48722 |
| student_id_S6531 |       -3.23162 |
| student_id_S6532 |        5.74676 |
| student_id_S6533 |       14.4161  |
| student_id_S6534 |        4.15079 |
| student_id_S6535 |        7.3775  |

---

### Blocco 525 (Feature 5241 - 5250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6536 |       19.1305  |
| student_id_S6537 |       -5.83856 |
| student_id_S6538 |      -13.1929  |
| student_id_S6539 |       -2.58426 |
| student_id_S6540 |      -10.6385  |
| student_id_S6541 |       -1.63966 |
| student_id_S6543 |        3.25938 |
| student_id_S6544 |        8.73939 |
| student_id_S6545 |       -1.99086 |
| student_id_S6546 |       -7.39163 |

---

### Blocco 526 (Feature 5251 - 5260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6547 |        3.77317 |
| student_id_S6548 |       11.3834  |
| student_id_S6549 |        2.20738 |
| student_id_S6550 |       -8.02918 |
| student_id_S6551 |        6.28225 |
| student_id_S6552 |       -7.41738 |
| student_id_S6553 |       -2.68786 |
| student_id_S6554 |       10.4634  |
| student_id_S6555 |      -11.1659  |
| student_id_S6556 |        5.18393 |

---

### Blocco 527 (Feature 5261 - 5270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6558 |      -5.7177   |
| student_id_S656  |       8.22938  |
| student_id_S6561 |      -8.13449  |
| student_id_S6562 |       4.47782  |
| student_id_S6563 |       3.63587  |
| student_id_S6564 |      -3.41286  |
| student_id_S6565 |      -2.57293  |
| student_id_S6566 |     -10.2507   |
| student_id_S6567 |      -7.15806  |
| student_id_S6568 |       0.999199 |

---

### Blocco 528 (Feature 5271 - 5280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6569 |      12.1159   |
| student_id_S6570 |      -6.26463  |
| student_id_S6571 |      11.5149   |
| student_id_S6572 |      -1.15693  |
| student_id_S6573 |      -0.178693 |
| student_id_S6574 |       5.74492  |
| student_id_S6575 |       2.31304  |
| student_id_S6576 |       6.1187   |
| student_id_S6577 |      -1.62511  |
| student_id_S6578 |      10.7391   |

---

### Blocco 529 (Feature 5281 - 5290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6579 |        2.07661 |
| student_id_S658  |        2.13109 |
| student_id_S6580 |       -8.01041 |
| student_id_S6583 |        2.12154 |
| student_id_S6584 |       12.5548  |
| student_id_S6586 |       -8.53498 |
| student_id_S6588 |        3.20615 |
| student_id_S6589 |       -5.07383 |
| student_id_S659  |       -8.92552 |
| student_id_S6590 |       17.5777  |

---

### Blocco 530 (Feature 5291 - 5300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6591 |        7.92492 |
| student_id_S6592 |        7.06487 |
| student_id_S6593 |        2.164   |
| student_id_S6595 |       -3.45003 |
| student_id_S6596 |       -4.11296 |
| student_id_S6597 |       -3.20489 |
| student_id_S6599 |       -7.60138 |
| student_id_S66   |       -7.50614 |
| student_id_S660  |        8.91142 |
| student_id_S6601 |        2.13685 |

---

### Blocco 531 (Feature 5301 - 5310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6602 |      -11.2681  |
| student_id_S6603 |        4.85747 |
| student_id_S6604 |       -1.86309 |
| student_id_S6605 |      -10.0937  |
| student_id_S6606 |       10.7679  |
| student_id_S6607 |       -6.05966 |
| student_id_S6608 |       -5.88628 |
| student_id_S661  |        7.52282 |
| student_id_S6610 |       -6.73801 |
| student_id_S6611 |       -5.61482 |

---

### Blocco 532 (Feature 5311 - 5320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6612 |    -14.2287    |
| student_id_S6614 |     -0.99198   |
| student_id_S6615 |     -0.0985164 |
| student_id_S6616 |     11.1523    |
| student_id_S6618 |     16.5069    |
| student_id_S6619 |     -9.20767   |
| student_id_S662  |     -3.75827   |
| student_id_S6621 |      9.03157   |
| student_id_S6622 |      9.3252    |
| student_id_S6623 |    -10.56      |

---

### Blocco 533 (Feature 5321 - 5330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6624 |      2.32077   |
| student_id_S6626 |      2.87888   |
| student_id_S6627 |    -11.5957    |
| student_id_S6629 |      0.716682  |
| student_id_S663  |      3.62233   |
| student_id_S6630 |     -2.99519   |
| student_id_S6631 |      1.33716   |
| student_id_S6633 |      0.0507186 |
| student_id_S6634 |    -10.0887    |
| student_id_S6635 |      6.3365    |

---

### Blocco 534 (Feature 5331 - 5340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6636 |       10.8132  |
| student_id_S6637 |       -2.78486 |
| student_id_S6638 |        3.53665 |
| student_id_S6639 |       10.9284  |
| student_id_S664  |      -12.0699  |
| student_id_S6640 |        1.51949 |
| student_id_S6641 |        5.67484 |
| student_id_S6642 |       -4.78897 |
| student_id_S6644 |        7.1032  |
| student_id_S6646 |       -8.89381 |

---

### Blocco 535 (Feature 5341 - 5350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6647 |      6.88784   |
| student_id_S6648 |     -3.08487   |
| student_id_S6649 |     -5.68888   |
| student_id_S665  |      4.48975   |
| student_id_S6650 |     -2.08056   |
| student_id_S6652 |     -6.97833   |
| student_id_S6655 |     -6.8226    |
| student_id_S6656 |      4.81918   |
| student_id_S6658 |     -0.0836782 |
| student_id_S6659 |      0.355926  |

---

### Blocco 536 (Feature 5351 - 5360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S666  |       -1.25445 |
| student_id_S6660 |        2.92565 |
| student_id_S6661 |       -6.08451 |
| student_id_S6662 |      -17.2309  |
| student_id_S6663 |       -1.99279 |
| student_id_S6664 |        8.64731 |
| student_id_S6665 |        6.86456 |
| student_id_S6666 |       -9.46294 |
| student_id_S6667 |       10.1045  |
| student_id_S6668 |      -10.5757  |

---

### Blocco 537 (Feature 5361 - 5370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6669 |      -0.972233 |
| student_id_S667  |      -1.45587  |
| student_id_S6670 |      11.0926   |
| student_id_S6671 |      -1.58024  |
| student_id_S6673 |       3.14672  |
| student_id_S6674 |      -4.60242  |
| student_id_S6676 |      -2.60482  |
| student_id_S6677 |      -7.64664  |
| student_id_S6678 |      10.4481   |
| student_id_S6679 |      -3.94353  |

---

### Blocco 538 (Feature 5371 - 5380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S668  |      -3.21712  |
| student_id_S6680 |       7.12821  |
| student_id_S6681 |       1.66098  |
| student_id_S6682 |      -5.43117  |
| student_id_S6683 |     -11.5348   |
| student_id_S6684 |       3.27489  |
| student_id_S6685 |       1.677    |
| student_id_S6686 |       1.80305  |
| student_id_S6687 |       0.471184 |
| student_id_S6689 |      -3.83071  |

---

### Blocco 539 (Feature 5381 - 5390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S669  |       15.1406  |
| student_id_S6690 |        8.81278 |
| student_id_S6691 |        6.68214 |
| student_id_S6692 |        6.75175 |
| student_id_S6693 |        2.43202 |
| student_id_S6694 |       -7.3121  |
| student_id_S6695 |       10.4882  |
| student_id_S6696 |       -3.39311 |
| student_id_S6697 |        2.47261 |
| student_id_S6698 |        2.87623 |

---

### Blocco 540 (Feature 5391 - 5400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S67   |       -1.7786  |
| student_id_S6700 |        2.36773 |
| student_id_S6701 |       -7.39423 |
| student_id_S6702 |       -5.39914 |
| student_id_S6703 |       14.6255  |
| student_id_S6705 |        2.79961 |
| student_id_S6706 |        3.99394 |
| student_id_S6707 |       17.1263  |
| student_id_S6708 |       -1.67032 |
| student_id_S6709 |       -6.51574 |

---

### Blocco 541 (Feature 5401 - 5410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S671  |       10.7531  |
| student_id_S6710 |      -12.3082  |
| student_id_S6711 |       -5.39657 |
| student_id_S6712 |       -3.60016 |
| student_id_S6713 |        8.1969  |
| student_id_S6715 |        7.88116 |
| student_id_S6716 |        0.17236 |
| student_id_S6717 |        5.4905  |
| student_id_S6718 |        6.25633 |
| student_id_S6719 |       -1.8804  |

---

### Blocco 542 (Feature 5411 - 5420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S672  |        6.85428 |
| student_id_S6720 |       -1.88474 |
| student_id_S6721 |       -5.43112 |
| student_id_S6722 |       -1.04714 |
| student_id_S6723 |       -4.25484 |
| student_id_S6725 |        9.66292 |
| student_id_S6726 |        2.12582 |
| student_id_S6727 |       -3.70249 |
| student_id_S6728 |        4.29787 |
| student_id_S6729 |        3.3394  |

---

### Blocco 543 (Feature 5421 - 5430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S673  |     -13.3804   |
| student_id_S6730 |       3.32311  |
| student_id_S6731 |       0.206063 |
| student_id_S6732 |      -6.83468  |
| student_id_S6733 |       0.988378 |
| student_id_S6734 |       3.4637   |
| student_id_S6735 |       6.60817  |
| student_id_S6736 |       5.07839  |
| student_id_S6737 |       1.84021  |
| student_id_S6739 |      -5.10213  |

---

### Blocco 544 (Feature 5431 - 5440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S674  |       -5.94068 |
| student_id_S6741 |        3.24025 |
| student_id_S6742 |       -7.71214 |
| student_id_S6743 |        2.56561 |
| student_id_S6744 |       -7.59718 |
| student_id_S6745 |       -1.58872 |
| student_id_S6746 |       -3.15038 |
| student_id_S6748 |        2.60674 |
| student_id_S6749 |      -10.5845  |
| student_id_S6750 |        5.80406 |

---

### Blocco 545 (Feature 5441 - 5450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6751 |       5.62021  |
| student_id_S6752 |       5.51723  |
| student_id_S6753 |       1.15746  |
| student_id_S6754 |      -2.65037  |
| student_id_S6755 |       2.51562  |
| student_id_S6756 |       2.45535  |
| student_id_S6758 |     -15.9771   |
| student_id_S6759 |      -0.187296 |
| student_id_S676  |       7.53814  |
| student_id_S6760 |      -3.43259  |

---

### Blocco 546 (Feature 5451 - 5460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6761 |      -3.52101  |
| student_id_S6762 |      -3.70264  |
| student_id_S6763 |      -5.30088  |
| student_id_S6765 |      -5.20312  |
| student_id_S6766 |      -6.46902  |
| student_id_S6767 |       6.89281  |
| student_id_S6768 |     -13.3719   |
| student_id_S6769 |       9.15409  |
| student_id_S677  |       0.151809 |
| student_id_S6770 |      -2.40947  |

---

### Blocco 547 (Feature 5461 - 5470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6771 |       -6.86356 |
| student_id_S6772 |        1.37832 |
| student_id_S6773 |       -4.75604 |
| student_id_S6774 |      -14.3133  |
| student_id_S6775 |        2.06275 |
| student_id_S6776 |       -7.47569 |
| student_id_S6777 |        1.91136 |
| student_id_S6778 |       -9.41    |
| student_id_S6779 |       -5.41768 |
| student_id_S678  |        2.7603  |

---

### Blocco 548 (Feature 5471 - 5480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6780 |      -0.709069 |
| student_id_S6781 |      15.3116   |
| student_id_S6782 |       3.55501  |
| student_id_S6783 |       1.85516  |
| student_id_S6785 |       0.492831 |
| student_id_S6788 |      -0.252118 |
| student_id_S6789 |      17.1096   |
| student_id_S679  |      -2.82204  |
| student_id_S6790 |     -11.3821   |
| student_id_S6791 |      -0.264489 |

---

### Blocco 549 (Feature 5481 - 5490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6793 |      15.785    |
| student_id_S6794 |      -6.03696  |
| student_id_S6795 |      -5.87826  |
| student_id_S6796 |      -2.11437  |
| student_id_S6798 |      -1.03321  |
| student_id_S6799 |     -12.6905   |
| student_id_S68   |       7.54013  |
| student_id_S680  |       0.299668 |
| student_id_S6800 |      -3.25473  |
| student_id_S6801 |      -0.129372 |

---

### Blocco 550 (Feature 5491 - 5500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6802 |       -4.54543 |
| student_id_S6803 |        1.03868 |
| student_id_S6806 |        3.07632 |
| student_id_S6807 |       -8.60312 |
| student_id_S6808 |       -7.89777 |
| student_id_S6809 |        7.90461 |
| student_id_S6810 |        1.01415 |
| student_id_S6812 |        3.1027  |
| student_id_S6813 |       -7.01144 |
| student_id_S6814 |       -7.43871 |

---

### Blocco 551 (Feature 5501 - 5510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6815 |     -10.8014   |
| student_id_S6816 |      -0.166187 |
| student_id_S6817 |       7.64793  |
| student_id_S6818 |      -9.09053  |
| student_id_S682  |       4.3574   |
| student_id_S6820 |      10.6443   |
| student_id_S6821 |       3.55249  |
| student_id_S6822 |      -6.50846  |
| student_id_S6823 |       8.09933  |
| student_id_S6824 |      -4.41167  |

---

### Blocco 552 (Feature 5511 - 5520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6825 |      -9.9428   |
| student_id_S6826 |      12.9419   |
| student_id_S6827 |       5.85254  |
| student_id_S6828 |      -7.78538  |
| student_id_S6829 |      -8.83812  |
| student_id_S683  |      -0.187102 |
| student_id_S6830 |      -2.11915  |
| student_id_S6831 |       6.99106  |
| student_id_S6832 |       2.0854   |
| student_id_S6833 |       0.78768  |

---

### Blocco 553 (Feature 5521 - 5530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6834 |       12.2587  |
| student_id_S6836 |       10.724   |
| student_id_S6838 |       -2.4575  |
| student_id_S6839 |       -1.26019 |
| student_id_S684  |       -3.65421 |
| student_id_S6840 |       -3.35121 |
| student_id_S6842 |       -7.82223 |
| student_id_S6843 |        2.18285 |
| student_id_S6844 |       -4.84133 |
| student_id_S6845 |        8.15312 |

---

### Blocco 554 (Feature 5531 - 5540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6846 |      11.4163   |
| student_id_S6847 |       0.937964 |
| student_id_S6848 |       3.79158  |
| student_id_S6849 |       4.86907  |
| student_id_S685  |      -4.4876   |
| student_id_S6850 |      14.5178   |
| student_id_S6851 |      12.9754   |
| student_id_S6852 |     -16.4118   |
| student_id_S6853 |      -7.53807  |
| student_id_S6854 |      11.9129   |

---

### Blocco 555 (Feature 5541 - 5550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6855 |       -6.0393  |
| student_id_S6856 |       -1.33502 |
| student_id_S6857 |      -10.4051  |
| student_id_S6859 |       -5.09471 |
| student_id_S686  |       11.7738  |
| student_id_S6860 |      -10.2823  |
| student_id_S6862 |       -3.17233 |
| student_id_S6864 |       -2.18178 |
| student_id_S6865 |      -11.3412  |
| student_id_S6866 |        6.43989 |

---

### Blocco 556 (Feature 5551 - 5560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6867 |        4.29114 |
| student_id_S6868 |       -6.11279 |
| student_id_S6869 |       14.6149  |
| student_id_S687  |       -2.28877 |
| student_id_S6870 |       -6.46258 |
| student_id_S6871 |       -1.54437 |
| student_id_S6872 |        8.49656 |
| student_id_S6874 |        2.29911 |
| student_id_S6875 |      -10.1558  |
| student_id_S6876 |      -10.1345  |

---

### Blocco 557 (Feature 5561 - 5570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6877 |      -0.358716 |
| student_id_S6878 |       4.04161  |
| student_id_S6879 |      -7.02934  |
| student_id_S688  |       5.18436  |
| student_id_S6880 |      -4.30209  |
| student_id_S6882 |      11.0743   |
| student_id_S6883 |      -2.18691  |
| student_id_S6884 |      -1.30007  |
| student_id_S6885 |       1.67649  |
| student_id_S6887 |      -7.07284  |

---

### Blocco 558 (Feature 5571 - 5580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6888 |       -3.04424 |
| student_id_S6889 |        7.59924 |
| student_id_S689  |        9.44048 |
| student_id_S6890 |       -6.4409  |
| student_id_S6891 |       -1.86806 |
| student_id_S6893 |       -1.83581 |
| student_id_S6894 |        3.05868 |
| student_id_S6896 |       -1.06508 |
| student_id_S6898 |       -3.29541 |
| student_id_S69   |        3.28851 |

---

### Blocco 559 (Feature 5581 - 5590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S690  |     -7.31654   |
| student_id_S6901 |     12.2204    |
| student_id_S6902 |      7.4084    |
| student_id_S6903 |     -0.0384557 |
| student_id_S6904 |      6.98047   |
| student_id_S6906 |     -5.47973   |
| student_id_S6907 |     -7.66337   |
| student_id_S6908 |      6.58395   |
| student_id_S691  |     -5.22711   |
| student_id_S6911 |      9.14547   |

---

### Blocco 560 (Feature 5591 - 5600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6912 |        3.7365  |
| student_id_S6913 |        6.39358 |
| student_id_S6914 |       -3.82246 |
| student_id_S6915 |        8.17393 |
| student_id_S6917 |      -10.5     |
| student_id_S6918 |        9.07027 |
| student_id_S6919 |      -10.526   |
| student_id_S692  |        9.87702 |
| student_id_S6920 |        8.15372 |
| student_id_S6921 |       14.12    |

---

### Blocco 561 (Feature 5601 - 5610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6922 |      -4.71344  |
| student_id_S6923 |      -1.61758  |
| student_id_S6924 |      -8.82201  |
| student_id_S6925 |      -0.957892 |
| student_id_S6927 |       7.78499  |
| student_id_S6928 |      -2.9627   |
| student_id_S6929 |      10.9414   |
| student_id_S693  |       1.72187  |
| student_id_S6930 |      -6.13046  |
| student_id_S6931 |     -14.465    |

---

### Blocco 562 (Feature 5611 - 5620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6932 |      -2.90723  |
| student_id_S6933 |      -1.04239  |
| student_id_S6934 |       6.06532  |
| student_id_S6935 |      -4.92817  |
| student_id_S6936 |       0.912932 |
| student_id_S6937 |       3.38586  |
| student_id_S6938 |     -10.6711   |
| student_id_S6939 |       1.62976  |
| student_id_S694  |      -0.542962 |
| student_id_S6940 |       1.13988  |

---

### Blocco 563 (Feature 5621 - 5630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6941 |       9.75966  |
| student_id_S6942 |      -6.82024  |
| student_id_S6943 |       8.42194  |
| student_id_S6944 |       2.66311  |
| student_id_S6945 |       6.5751   |
| student_id_S6946 |       6.42212  |
| student_id_S6947 |      -0.940206 |
| student_id_S6948 |       1.2045   |
| student_id_S6949 |       4.3847   |
| student_id_S695  |       0.746299 |

---

### Blocco 564 (Feature 5631 - 5640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6950 |       9.21256  |
| student_id_S6951 |      -3.75705  |
| student_id_S6952 |       6.15618  |
| student_id_S6953 |      12.6414   |
| student_id_S6954 |       0.643884 |
| student_id_S6955 |       2.00554  |
| student_id_S6956 |     -10.7161   |
| student_id_S6957 |       5.89852  |
| student_id_S6958 |       9.9707   |
| student_id_S6960 |      10.1663   |

---

### Blocco 565 (Feature 5641 - 5650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6962 |        2.97202 |
| student_id_S6964 |       -1.31511 |
| student_id_S6965 |       -5.64686 |
| student_id_S6966 |        2.12763 |
| student_id_S6967 |        6.06555 |
| student_id_S6968 |        5.94276 |
| student_id_S6969 |       -6.53573 |
| student_id_S697  |       -2.8239  |
| student_id_S6970 |       -3.04216 |
| student_id_S6971 |       10.285   |

---

### Blocco 566 (Feature 5651 - 5660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6972 |       -6.86012 |
| student_id_S6973 |        1.90669 |
| student_id_S6974 |        6.66873 |
| student_id_S6975 |       -1.66651 |
| student_id_S6976 |       -1.43365 |
| student_id_S6977 |        3.89707 |
| student_id_S6978 |      -11.5588  |
| student_id_S6979 |       10.42    |
| student_id_S698  |        7.4483  |
| student_id_S6980 |        6.07658 |

---

### Blocco 567 (Feature 5661 - 5670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6981 |       5.13024  |
| student_id_S6982 |      -1.46382  |
| student_id_S6983 |      -5.58694  |
| student_id_S6984 |      -6.52232  |
| student_id_S6986 |      -9.03742  |
| student_id_S6988 |       3.23467  |
| student_id_S6989 |      -8.14664  |
| student_id_S699  |      -7.26427  |
| student_id_S6990 |      -0.848339 |
| student_id_S6992 |      -3.75491  |

---

### Blocco 568 (Feature 5671 - 5680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S6993 |       5.81846  |
| student_id_S6994 |       1.73777  |
| student_id_S6997 |      10.002    |
| student_id_S6998 |       0.940198 |
| student_id_S6999 |      -8.26457  |
| student_id_S7    |      -6.71357  |
| student_id_S70   |      -9.56628  |
| student_id_S700  |      -8.97065  |
| student_id_S7000 |      -0.172433 |
| student_id_S7001 |       4.00042  |

---

### Blocco 569 (Feature 5681 - 5690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7002 |       7.60353  |
| student_id_S7003 |       2.09026  |
| student_id_S7004 |      -4.83839  |
| student_id_S7005 |     -13.9117   |
| student_id_S7006 |      -2.10929  |
| student_id_S7007 |     -10.2391   |
| student_id_S7008 |      -9.25131  |
| student_id_S701  |     -13.0986   |
| student_id_S7010 |       0.102421 |
| student_id_S7011 |      -0.033443 |

---

### Blocco 570 (Feature 5691 - 5700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7012 |      -0.470066 |
| student_id_S7013 |      -4.55782  |
| student_id_S7014 |      -0.120743 |
| student_id_S7015 |      -5.41907  |
| student_id_S7016 |       5.26312  |
| student_id_S7017 |      -5.27907  |
| student_id_S7018 |       1.72666  |
| student_id_S7019 |      -7.94378  |
| student_id_S7020 |      -4.03477  |
| student_id_S7021 |      -3.57775  |

---

### Blocco 571 (Feature 5701 - 5710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7022 |       1.51973  |
| student_id_S7023 |      -1.15132  |
| student_id_S7024 |       5.26038  |
| student_id_S7025 |      -0.968945 |
| student_id_S7026 |      -5.80654  |
| student_id_S7027 |      -6.21706  |
| student_id_S7028 |      11.4068   |
| student_id_S7029 |      -4.36668  |
| student_id_S703  |       8.83443  |
| student_id_S7030 |      -0.775036 |

---

### Blocco 572 (Feature 5711 - 5720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7032 |       4.35252  |
| student_id_S7033 |      -0.304391 |
| student_id_S7034 |      -0.856441 |
| student_id_S7035 |      -4.27789  |
| student_id_S7036 |     -12.5823   |
| student_id_S7037 |       5.44876  |
| student_id_S7039 |      -2.17019  |
| student_id_S704  |      -4.29509  |
| student_id_S7040 |       4.28202  |
| student_id_S7042 |       0.571031 |

---

### Blocco 573 (Feature 5721 - 5730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7043 |       -2.65454 |
| student_id_S7044 |       -9.60224 |
| student_id_S7046 |       -2.60365 |
| student_id_S7047 |        2.40246 |
| student_id_S7048 |        3.87639 |
| student_id_S7049 |        3.77094 |
| student_id_S705  |       10.1159  |
| student_id_S7050 |        5.04538 |
| student_id_S7051 |       -7.42426 |
| student_id_S7052 |       -8.34071 |

---

### Blocco 574 (Feature 5731 - 5740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7053 |       1.31912  |
| student_id_S7054 |      12.1131   |
| student_id_S7055 |      -5.52423  |
| student_id_S7056 |       1.79211  |
| student_id_S7057 |       1.42947  |
| student_id_S7058 |      -0.704133 |
| student_id_S7059 |       1.68553  |
| student_id_S706  |      -2.19027  |
| student_id_S7060 |      -5.94877  |
| student_id_S7061 |      -1.90855  |

---

### Blocco 575 (Feature 5741 - 5750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7063 |      -0.547509 |
| student_id_S7066 |      -3.867    |
| student_id_S7067 |      -0.789675 |
| student_id_S7068 |       4.94059  |
| student_id_S7069 |     -10.8723   |
| student_id_S707  |      -6.78514  |
| student_id_S7070 |       5.65835  |
| student_id_S7071 |     -12.5747   |
| student_id_S7072 |       6.41496  |
| student_id_S7073 |      -5.84881  |

---

### Blocco 576 (Feature 5751 - 5760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7074 |        6.13252 |
| student_id_S7075 |        4.61697 |
| student_id_S7077 |      -10.6001  |
| student_id_S7079 |       -4.77185 |
| student_id_S708  |       13.9313  |
| student_id_S7080 |       -5.08745 |
| student_id_S7081 |       -5.35696 |
| student_id_S7082 |       -2.50118 |
| student_id_S7083 |       -3.44147 |
| student_id_S7084 |       -2.62402 |

---

### Blocco 577 (Feature 5761 - 5770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7085 |        2.63977 |
| student_id_S7086 |       -3.14272 |
| student_id_S7087 |       -8.88058 |
| student_id_S7088 |        3.48222 |
| student_id_S7089 |       -1.14107 |
| student_id_S709  |       -7.16689 |
| student_id_S7090 |        5.56548 |
| student_id_S7091 |        2.07967 |
| student_id_S7092 |       -3.06209 |
| student_id_S7093 |       -7.5385  |

---

### Blocco 578 (Feature 5771 - 5780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7094 |       0.226806 |
| student_id_S7095 |      -8.23381  |
| student_id_S7096 |      -2.96238  |
| student_id_S7097 |      -5.62173  |
| student_id_S7098 |       5.01315  |
| student_id_S7099 |      -0.34616  |
| student_id_S710  |       4.584    |
| student_id_S7100 |       0.687134 |
| student_id_S7101 |      -6.3829   |
| student_id_S7102 |      -2.21602  |

---

### Blocco 579 (Feature 5781 - 5790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7103 |        2.73883 |
| student_id_S7104 |        2.48172 |
| student_id_S7105 |       -5.32715 |
| student_id_S7106 |        7.40079 |
| student_id_S7108 |       -1.20558 |
| student_id_S7109 |        4.78898 |
| student_id_S711  |       13.5431  |
| student_id_S7110 |      -12.504   |
| student_id_S7111 |       -6.53608 |
| student_id_S7112 |       10.2701  |

---

### Blocco 580 (Feature 5791 - 5800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7113 |      -6.84643  |
| student_id_S7114 |       1.55073  |
| student_id_S7115 |     -10.8904   |
| student_id_S7116 |       7.32283  |
| student_id_S7117 |      -1.15213  |
| student_id_S7119 |       6.89129  |
| student_id_S712  |       4.71879  |
| student_id_S7120 |      -5.67095  |
| student_id_S7121 |      -1.4513   |
| student_id_S7123 |       0.819645 |

---

### Blocco 581 (Feature 5801 - 5810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7126 |       2.9226   |
| student_id_S7127 |       0.465534 |
| student_id_S7128 |      -1.92205  |
| student_id_S7129 |      -2.35201  |
| student_id_S713  |      -3.01569  |
| student_id_S7130 |      -4.18552  |
| student_id_S7131 |       0.596072 |
| student_id_S7133 |       2.71352  |
| student_id_S7134 |      -1.15427  |
| student_id_S7135 |       1.21532  |

---

### Blocco 582 (Feature 5811 - 5820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7136 |       1.7175   |
| student_id_S7137 |     -12.4387   |
| student_id_S7139 |       0.279145 |
| student_id_S714  |       1.85648  |
| student_id_S7140 |      -1.35433  |
| student_id_S7141 |      11.4943   |
| student_id_S7142 |     -12.9226   |
| student_id_S7143 |      -3.79918  |
| student_id_S7145 |       5.57395  |
| student_id_S7146 |     -11.3162   |

---

### Blocco 583 (Feature 5821 - 5830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7147 |      10.5618   |
| student_id_S7148 |     -15.9265   |
| student_id_S7149 |       7.28519  |
| student_id_S715  |      -0.129615 |
| student_id_S7150 |      -8.72095  |
| student_id_S7152 |      -0.875452 |
| student_id_S7153 |       4.68263  |
| student_id_S7154 |       0.719223 |
| student_id_S7155 |       4.35708  |
| student_id_S7157 |      -2.10977  |

---

### Blocco 584 (Feature 5831 - 5840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7158 |        5.96262 |
| student_id_S7159 |       -5.92144 |
| student_id_S716  |       -1.98936 |
| student_id_S7160 |       -6.13349 |
| student_id_S7161 |        2.56588 |
| student_id_S7162 |        1.63161 |
| student_id_S7163 |        7.80616 |
| student_id_S7164 |        6.58292 |
| student_id_S7165 |       -5.96837 |
| student_id_S7166 |        9.09069 |

---

### Blocco 585 (Feature 5841 - 5850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7167 |      -4.35577  |
| student_id_S7169 |      -7.84145  |
| student_id_S717  |     -11.8196   |
| student_id_S7170 |      -7.98763  |
| student_id_S7171 |      -3.41268  |
| student_id_S7172 |       8.10269  |
| student_id_S7173 |       0.770965 |
| student_id_S7174 |      -6.95482  |
| student_id_S7175 |      -8.91347  |
| student_id_S7176 |       5.21598  |

---

### Blocco 586 (Feature 5851 - 5860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7177 |      10.0104   |
| student_id_S7178 |       4.63007  |
| student_id_S7179 |       1.61139  |
| student_id_S718  |       5.13286  |
| student_id_S7180 |      -0.781612 |
| student_id_S7181 |       2.67073  |
| student_id_S7182 |      14.3454   |
| student_id_S7183 |       3.97296  |
| student_id_S7185 |      -2.72897  |
| student_id_S7186 |      -4.92895  |

---

### Blocco 587 (Feature 5861 - 5870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7187 |      -1.93467  |
| student_id_S7189 |       1.128    |
| student_id_S719  |       0.890284 |
| student_id_S7191 |       0.7099   |
| student_id_S7192 |      -2.59728  |
| student_id_S7194 |      -1.16788  |
| student_id_S7195 |       0.457915 |
| student_id_S7196 |      -8.16832  |
| student_id_S7197 |       6.10307  |
| student_id_S7199 |      -4.09064  |

---

### Blocco 588 (Feature 5871 - 5880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7200 |      15.0193   |
| student_id_S7201 |     -10.9793   |
| student_id_S7202 |      -6.58355  |
| student_id_S7203 |       5.26823  |
| student_id_S7204 |      -3.04557  |
| student_id_S7205 |     -10.1262   |
| student_id_S7206 |       0.973913 |
| student_id_S7207 |      -0.281675 |
| student_id_S7208 |      -8.34662  |
| student_id_S7210 |       3.45975  |

---

### Blocco 589 (Feature 5881 - 5890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7211 |       3.31493  |
| student_id_S7212 |      -0.524144 |
| student_id_S7214 |      -2.23198  |
| student_id_S7217 |      -2.93033  |
| student_id_S7218 |      -1.69496  |
| student_id_S7219 |     -14.5541   |
| student_id_S722  |      -8.3067   |
| student_id_S7220 |      -3.05468  |
| student_id_S7221 |       4.75979  |
| student_id_S7222 |      11.4398   |

---

### Blocco 590 (Feature 5891 - 5900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7223 |      16.6027   |
| student_id_S7224 |       0.700848 |
| student_id_S7227 |      18.1369   |
| student_id_S7229 |      -6.07968  |
| student_id_S723  |       8.49783  |
| student_id_S7231 |       9.50925  |
| student_id_S7233 |       6.27446  |
| student_id_S7235 |       3.50093  |
| student_id_S7237 |      -0.530007 |
| student_id_S7239 |     -10.4485   |

---

### Blocco 591 (Feature 5901 - 5910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S724  |      -0.783292 |
| student_id_S7240 |      -4.10432  |
| student_id_S7241 |       9.44998  |
| student_id_S7242 |      -2.76534  |
| student_id_S7243 |      -4.66114  |
| student_id_S7244 |      -5.88165  |
| student_id_S7245 |      -0.980319 |
| student_id_S7246 |       2.81842  |
| student_id_S7248 |       2.32953  |
| student_id_S7249 |      14.4965   |

---

### Blocco 592 (Feature 5911 - 5920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S725  |        9.4082  |
| student_id_S7250 |       -7.40225 |
| student_id_S7251 |       -2.39284 |
| student_id_S7252 |       -5.87411 |
| student_id_S7253 |       -4.43211 |
| student_id_S7254 |       13.3788  |
| student_id_S7255 |        1.02538 |
| student_id_S7256 |      -10.1132  |
| student_id_S7257 |       -5.61125 |
| student_id_S7258 |       11.2464  |

---

### Blocco 593 (Feature 5921 - 5930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7259 |       4.80488  |
| student_id_S726  |      -0.895568 |
| student_id_S7262 |      -0.712125 |
| student_id_S7263 |       2.43617  |
| student_id_S7264 |       4.04758  |
| student_id_S7265 |       6.34472  |
| student_id_S7266 |       6.12001  |
| student_id_S7267 |      -2.79082  |
| student_id_S7268 |      -2.27077  |
| student_id_S7269 |       7.42403  |

---

### Blocco 594 (Feature 5931 - 5940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S727  |       -8.71698 |
| student_id_S7270 |       -4.64306 |
| student_id_S7271 |        1.09908 |
| student_id_S7272 |        4.45888 |
| student_id_S7273 |        8.49608 |
| student_id_S7274 |       -4.71228 |
| student_id_S7275 |        8.00423 |
| student_id_S7276 |       10.6097  |
| student_id_S7277 |       15.4506  |
| student_id_S7278 |      -10.1739  |

---

### Blocco 595 (Feature 5941 - 5950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7279 |      -8.4657   |
| student_id_S7280 |      -4.29077  |
| student_id_S7281 |      -6.89605  |
| student_id_S7283 |     -11.6105   |
| student_id_S7285 |      -3.92774  |
| student_id_S7286 |      -3.02442  |
| student_id_S7287 |      -8.08823  |
| student_id_S7288 |      -0.356377 |
| student_id_S7289 |       5.0883   |
| student_id_S7290 |      -0.791213 |

---

### Blocco 596 (Feature 5951 - 5960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7292 |        1.42004 |
| student_id_S7293 |        5.0467  |
| student_id_S7294 |       -3.97314 |
| student_id_S7295 |      -18.6778  |
| student_id_S7296 |        7.94371 |
| student_id_S7297 |       10.0591  |
| student_id_S7299 |       -1.31233 |
| student_id_S73   |       -7.4998  |
| student_id_S7301 |        2.9704  |
| student_id_S7302 |       -1.65879 |

---

### Blocco 597 (Feature 5961 - 5970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7304 |      7.94635   |
| student_id_S7305 |     -6.35152   |
| student_id_S7306 |     -6.54288   |
| student_id_S7307 |      6.1701    |
| student_id_S7308 |     11.2691    |
| student_id_S7309 |     -0.0790133 |
| student_id_S731  |     -3.43278   |
| student_id_S7310 |      9.84546   |
| student_id_S7311 |     -4.11022   |
| student_id_S7312 |     -0.130849  |

---

### Blocco 598 (Feature 5971 - 5980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7313 |      -7.85732  |
| student_id_S7314 |       6.58188  |
| student_id_S7315 |       4.65887  |
| student_id_S7316 |       1.17498  |
| student_id_S7317 |       8.98912  |
| student_id_S7318 |      -1.04135  |
| student_id_S7319 |      -5.31108  |
| student_id_S732  |       2.64408  |
| student_id_S7320 |      -0.503052 |
| student_id_S7321 |       8.10226  |

---

### Blocco 599 (Feature 5981 - 5990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7322 |       4.9094   |
| student_id_S7323 |       9.68241  |
| student_id_S7324 |       7.95431  |
| student_id_S7325 |       6.78243  |
| student_id_S7326 |      -0.923757 |
| student_id_S7327 |       8.22568  |
| student_id_S7328 |      -3.54637  |
| student_id_S7329 |       1.42212  |
| student_id_S733  |       6.72049  |
| student_id_S7330 |      -9.21961  |

---

### Blocco 600 (Feature 5991 - 6000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7331 |       0.932261 |
| student_id_S7332 |      -9.57045  |
| student_id_S7334 |      -0.283565 |
| student_id_S7335 |       4.3888   |
| student_id_S7336 |      -0.477287 |
| student_id_S7337 |      -5.21297  |
| student_id_S7338 |       5.65456  |
| student_id_S7339 |       1.19381  |
| student_id_S734  |      -2.58909  |
| student_id_S7340 |     -11.8169   |

---

### Blocco 601 (Feature 6001 - 6010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7341 |       14.8224  |
| student_id_S7342 |       10.077   |
| student_id_S7343 |       -2.90728 |
| student_id_S7345 |      -14.2637  |
| student_id_S7346 |        4.86633 |
| student_id_S7347 |       -2.61691 |
| student_id_S7348 |        1.56794 |
| student_id_S7349 |       -5.50337 |
| student_id_S735  |      -11.8876  |
| student_id_S7350 |       -7.27191 |

---

### Blocco 602 (Feature 6011 - 6020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7351 |      -0.322415 |
| student_id_S7352 |      -3.70167  |
| student_id_S7354 |      13.4722   |
| student_id_S7355 |       9.98664  |
| student_id_S7356 |       0.575893 |
| student_id_S7357 |      -2.52826  |
| student_id_S7358 |       0.85585  |
| student_id_S7359 |       4.08387  |
| student_id_S736  |       3.65411  |
| student_id_S7360 |      -5.19102  |

---

### Blocco 603 (Feature 6021 - 6030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7361 |        9.28725 |
| student_id_S7362 |        1.91988 |
| student_id_S7363 |       -8.8481  |
| student_id_S7364 |        3.64377 |
| student_id_S7365 |       -7.66033 |
| student_id_S7366 |       -2.7725  |
| student_id_S7367 |       -3.27352 |
| student_id_S7368 |      -12.8416  |
| student_id_S7369 |        1.98587 |
| student_id_S737  |        1.14855 |

---

### Blocco 604 (Feature 6031 - 6040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7370 |      -9.74438  |
| student_id_S7371 |      11.0702   |
| student_id_S7372 |       4.84166  |
| student_id_S7373 |       0.710775 |
| student_id_S7374 |       6.12649  |
| student_id_S7376 |       7.96225  |
| student_id_S7377 |      13.0692   |
| student_id_S7378 |      -7.75684  |
| student_id_S7379 |       4.28966  |
| student_id_S738  |       4.6063   |

---

### Blocco 605 (Feature 6041 - 6050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7380 |      -13.6076  |
| student_id_S7381 |       -4.06553 |
| student_id_S7382 |       10.9852  |
| student_id_S7383 |        3.92577 |
| student_id_S7384 |       -7.57081 |
| student_id_S7385 |       -3.71834 |
| student_id_S7386 |        6.89523 |
| student_id_S7387 |        1.24699 |
| student_id_S7388 |        3.20963 |
| student_id_S7389 |       11.1312  |

---

### Blocco 606 (Feature 6051 - 6060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7390 |      -14.377   |
| student_id_S7392 |        7.10052 |
| student_id_S7393 |      -17.2886  |
| student_id_S7394 |       -4.82448 |
| student_id_S7395 |        8.99638 |
| student_id_S7396 |        5.0919  |
| student_id_S7397 |       10.851   |
| student_id_S7398 |       -2.29008 |
| student_id_S7399 |        5.64582 |
| student_id_S74   |        3.91798 |

---

### Blocco 607 (Feature 6061 - 6070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S740  |     -6.22492   |
| student_id_S7401 |     -5.02202   |
| student_id_S7402 |     -8.89403   |
| student_id_S7403 |     11.8622    |
| student_id_S7404 |     -2.82276   |
| student_id_S7405 |     -0.0395016 |
| student_id_S7406 |      4.78265   |
| student_id_S7407 |      5.26752   |
| student_id_S7408 |     -6.11875   |
| student_id_S7409 |      9.06183   |

---

### Blocco 608 (Feature 6071 - 6080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7410 |      -9.62881  |
| student_id_S7411 |      -7.29475  |
| student_id_S7412 |      -5.96815  |
| student_id_S7413 |       1.5062   |
| student_id_S7414 |      -9.4126   |
| student_id_S7415 |       1.38725  |
| student_id_S7416 |      -5.36557  |
| student_id_S7417 |      -7.27119  |
| student_id_S7419 |      -3.83194  |
| student_id_S742  |       0.226528 |

---

### Blocco 609 (Feature 6081 - 6090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7420 |      -4.00849  |
| student_id_S7422 |      -5.38151  |
| student_id_S7423 |      -2.6957   |
| student_id_S7424 |     -13.2987   |
| student_id_S7425 |       0.775997 |
| student_id_S7426 |       5.96619  |
| student_id_S7427 |      -9.45722  |
| student_id_S7428 |       1.27531  |
| student_id_S7429 |       3.18974  |
| student_id_S743  |       5.36704  |

---

### Blocco 610 (Feature 6091 - 6100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7430 |      -5.51564  |
| student_id_S7431 |      -1.08537  |
| student_id_S7432 |      10.5954   |
| student_id_S7434 |      -6.95269  |
| student_id_S7435 |      11.812    |
| student_id_S7436 |       9.65971  |
| student_id_S7437 |     -11.9713   |
| student_id_S7439 |      -5.78414  |
| student_id_S744  |      -0.589313 |
| student_id_S7440 |      -4.49008  |

---

### Blocco 611 (Feature 6101 - 6110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7441 |     -0.0336178 |
| student_id_S7443 |     -6.84343   |
| student_id_S7444 |     -6.20441   |
| student_id_S7445 |     -3.64048   |
| student_id_S7446 |      4.47212   |
| student_id_S7447 |      3.41461   |
| student_id_S7448 |     -4.13583   |
| student_id_S7449 |     -7.94856   |
| student_id_S7450 |      1.75061   |
| student_id_S7451 |      4.78351   |

---

### Blocco 612 (Feature 6111 - 6120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7452 |      4.39113   |
| student_id_S7453 |    -12.4918    |
| student_id_S7454 |     -5.08707   |
| student_id_S7455 |      0.0253063 |
| student_id_S7456 |      1.32114   |
| student_id_S7458 |      4.03391   |
| student_id_S7459 |      2.66003   |
| student_id_S746  |    -10.8795    |
| student_id_S7460 |     -0.127398  |
| student_id_S7461 |      0.676347  |

---

### Blocco 613 (Feature 6121 - 6130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7462 |       3.91787  |
| student_id_S7463 |      -7.78045  |
| student_id_S7464 |      -0.978408 |
| student_id_S7465 |      -2.19404  |
| student_id_S7466 |      -5.61098  |
| student_id_S7467 |      -5.39592  |
| student_id_S7468 |       7.07614  |
| student_id_S7469 |      -8.10028  |
| student_id_S747  |      -0.708674 |
| student_id_S7470 |     -13.5538   |

---

### Blocco 614 (Feature 6131 - 6140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7471 |        3.35192 |
| student_id_S7472 |      -12.5913  |
| student_id_S7473 |      -13.337   |
| student_id_S7474 |        1.54785 |
| student_id_S7475 |      -12.3897  |
| student_id_S7476 |        2.71097 |
| student_id_S7477 |       11.3729  |
| student_id_S7478 |        3.82651 |
| student_id_S7479 |       10.1334  |
| student_id_S748  |       -8.14386 |

---

### Blocco 615 (Feature 6141 - 6150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7481 |        4.62241 |
| student_id_S7482 |        2.18203 |
| student_id_S7483 |        7.35535 |
| student_id_S7485 |       -4.14075 |
| student_id_S7487 |      -13.2832  |
| student_id_S7488 |       -6.27897 |
| student_id_S7489 |       -7.04796 |
| student_id_S749  |       12.3129  |
| student_id_S7490 |       12.0082  |
| student_id_S7491 |        3.66683 |

---

### Blocco 616 (Feature 6151 - 6160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7492 |       -6.23354 |
| student_id_S7493 |      -10.2139  |
| student_id_S7494 |        7.25398 |
| student_id_S7495 |       -3.07859 |
| student_id_S7496 |       -2.24551 |
| student_id_S7497 |      -11.2513  |
| student_id_S7498 |       -5.31074 |
| student_id_S7499 |       -8.04784 |
| student_id_S75   |       -1.66069 |
| student_id_S750  |        3.81602 |

---

### Blocco 617 (Feature 6161 - 6170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7500 |        5.15133 |
| student_id_S7501 |       -4.35385 |
| student_id_S7503 |       -2.28346 |
| student_id_S7504 |       -7.07256 |
| student_id_S7505 |        6.88845 |
| student_id_S7507 |        6.47261 |
| student_id_S7508 |        6.09011 |
| student_id_S7509 |        1.85418 |
| student_id_S751  |       -3.53785 |
| student_id_S7510 |        2.7706  |

---

### Blocco 618 (Feature 6171 - 6180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7511 |      10.1808   |
| student_id_S7512 |      -1.25863  |
| student_id_S7513 |      -1.5295   |
| student_id_S7514 |      10.7643   |
| student_id_S7515 |      -6.31567  |
| student_id_S7516 |       0.954074 |
| student_id_S7518 |      -4.11609  |
| student_id_S7519 |       7.82952  |
| student_id_S752  |     -11.0663   |
| student_id_S7520 |      -7.25705  |

---

### Blocco 619 (Feature 6181 - 6190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7521 |     -10.3597   |
| student_id_S7522 |      13.0711   |
| student_id_S7523 |      13.3708   |
| student_id_S7524 |      -0.938992 |
| student_id_S7525 |       9.71873  |
| student_id_S7526 |      -7.78277  |
| student_id_S7527 |      -4.97715  |
| student_id_S7528 |       7.23699  |
| student_id_S7529 |      11.6442   |
| student_id_S753  |      -2.14988  |

---

### Blocco 620 (Feature 6191 - 6200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7530 |       -5.93287 |
| student_id_S7531 |        3.19911 |
| student_id_S7532 |       -2.52453 |
| student_id_S7533 |       -1.78082 |
| student_id_S7534 |        4.85626 |
| student_id_S7535 |        1.43936 |
| student_id_S7537 |        7.52089 |
| student_id_S7538 |       -8.11046 |
| student_id_S7539 |       10.9118  |
| student_id_S754  |       -6.22555 |

---

### Blocco 621 (Feature 6201 - 6210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7541 |        7.44113 |
| student_id_S7542 |       10.2349  |
| student_id_S7543 |       -6.89542 |
| student_id_S7544 |       -1.00043 |
| student_id_S7545 |        6.54648 |
| student_id_S7546 |       -5.40308 |
| student_id_S7547 |       -9.44117 |
| student_id_S7548 |       -7.72326 |
| student_id_S7549 |       -5.62158 |
| student_id_S755  |       -8.4102  |

---

### Blocco 622 (Feature 6211 - 6220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7550 |      10.7414   |
| student_id_S7551 |      -7.1044   |
| student_id_S7552 |      -1.84317  |
| student_id_S7553 |      13.4673   |
| student_id_S7554 |      -5.90664  |
| student_id_S7555 |       3.92018  |
| student_id_S7557 |      -2.1102   |
| student_id_S7559 |      -2.03224  |
| student_id_S756  |       3.14899  |
| student_id_S7560 |       0.470533 |

---

### Blocco 623 (Feature 6221 - 6230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7561 |       0.200709 |
| student_id_S7562 |      -6.26397  |
| student_id_S7563 |       5.20447  |
| student_id_S7564 |     -10.4518   |
| student_id_S7565 |     -14.8772   |
| student_id_S7566 |      -3.31742  |
| student_id_S7569 |       3.14385  |
| student_id_S757  |      -7.84528  |
| student_id_S7570 |      -2.2829   |
| student_id_S7571 |      -7.69388  |

---

### Blocco 624 (Feature 6231 - 6240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7572 |      -1.47768  |
| student_id_S7573 |      -5.44617  |
| student_id_S7574 |       5.96302  |
| student_id_S7575 |      -1.9462   |
| student_id_S7576 |      -3.40497  |
| student_id_S7577 |      -0.227047 |
| student_id_S7578 |      -6.69767  |
| student_id_S7579 |      -1.88753  |
| student_id_S758  |       4.90833  |
| student_id_S7580 |       0.419188 |

---

### Blocco 625 (Feature 6241 - 6250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7581 |       1.65326  |
| student_id_S7582 |       0.523014 |
| student_id_S7583 |       2.52193  |
| student_id_S7584 |      11.6409   |
| student_id_S7586 |      -4.91929  |
| student_id_S7587 |       0.883349 |
| student_id_S7589 |       4.02304  |
| student_id_S7590 |      -2.81384  |
| student_id_S7591 |       3.40389  |
| student_id_S7592 |      10.7552   |

---

### Blocco 626 (Feature 6251 - 6260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7593 |      -7.12479  |
| student_id_S7595 |       3.30293  |
| student_id_S7596 |      -3.88044  |
| student_id_S7597 |       5.90208  |
| student_id_S7598 |      -7.91271  |
| student_id_S7599 |       0.851198 |
| student_id_S76   |       5.88965  |
| student_id_S760  |      10.493    |
| student_id_S7600 |      -3.43705  |
| student_id_S7601 |     -12.9655   |

---

### Blocco 627 (Feature 6261 - 6270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7602 |      -3.27398  |
| student_id_S7604 |     -11.7052   |
| student_id_S7605 |     -12.4522   |
| student_id_S7607 |       4.88287  |
| student_id_S7608 |      -0.237599 |
| student_id_S7609 |       1.93778  |
| student_id_S7610 |       8.5273   |
| student_id_S7611 |       3.05947  |
| student_id_S7612 |       2.84342  |
| student_id_S7613 |      -6.26624  |

---

### Blocco 628 (Feature 6271 - 6280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7614 |     -5.94582   |
| student_id_S7615 |     -6.80282   |
| student_id_S7616 |      0.255157  |
| student_id_S7617 |      9.06402   |
| student_id_S7619 |     -2.82741   |
| student_id_S762  |      8.62084   |
| student_id_S7620 |      6.94983   |
| student_id_S7621 |     -8.55083   |
| student_id_S7622 |     -0.0686807 |
| student_id_S7623 |      5.18529   |

---

### Blocco 629 (Feature 6281 - 6290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7625 |      -0.668149 |
| student_id_S7627 |      12.3374   |
| student_id_S7629 |       2.06422  |
| student_id_S763  |       4.26744  |
| student_id_S7630 |      13.1529   |
| student_id_S7632 |       8.59159  |
| student_id_S7633 |      -6.54203  |
| student_id_S7634 |       2.65478  |
| student_id_S7636 |       7.90911  |
| student_id_S7637 |      -6.59288  |

---

### Blocco 630 (Feature 6291 - 6300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7638 |       -1.77564 |
| student_id_S7639 |      -12.6759  |
| student_id_S764  |        7.11993 |
| student_id_S7640 |        8.74266 |
| student_id_S7641 |       -8.57952 |
| student_id_S7642 |        2.45027 |
| student_id_S7643 |        5.80486 |
| student_id_S7644 |       -5.50213 |
| student_id_S7646 |       -3.65562 |
| student_id_S7647 |       -1.18697 |

---

### Blocco 631 (Feature 6301 - 6310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7648 |       -3.69305 |
| student_id_S765  |       -5.87532 |
| student_id_S7650 |        1.50027 |
| student_id_S7651 |       -2.97057 |
| student_id_S7652 |        1.72872 |
| student_id_S7653 |      -11.5467  |
| student_id_S7654 |       16.8788  |
| student_id_S7655 |       -5.05862 |
| student_id_S7656 |        6.02216 |
| student_id_S7657 |       15.9225  |

---

### Blocco 632 (Feature 6311 - 6320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7658 |      -1.78443  |
| student_id_S7659 |       0.379923 |
| student_id_S766  |      -5.3972   |
| student_id_S7660 |      13.2097   |
| student_id_S7661 |       0.559814 |
| student_id_S7662 |      -4.15403  |
| student_id_S7663 |      -4.26956  |
| student_id_S7664 |      -1.3628   |
| student_id_S7665 |      11.1343   |
| student_id_S7666 |      -5.26865  |

---

### Blocco 633 (Feature 6321 - 6330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7668 |       5.53515  |
| student_id_S7669 |       9.70677  |
| student_id_S767  |       3.40402  |
| student_id_S7671 |       9.73371  |
| student_id_S7674 |      -3.91032  |
| student_id_S7675 |      -0.609401 |
| student_id_S7676 |      -5.07121  |
| student_id_S7677 |       3.91001  |
| student_id_S7678 |       1.84912  |
| student_id_S7679 |       2.72504  |

---

### Blocco 634 (Feature 6331 - 6340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S768  |       -3.33644 |
| student_id_S7680 |       -7.28945 |
| student_id_S7681 |       -5.82864 |
| student_id_S7682 |       11.5252  |
| student_id_S7683 |      -11.0248  |
| student_id_S7684 |       17.4336  |
| student_id_S7685 |        2.71556 |
| student_id_S7686 |        9.68642 |
| student_id_S7687 |       -6.39095 |
| student_id_S7689 |       -1.90216 |

---

### Blocco 635 (Feature 6341 - 6350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S769  |       -8.40576 |
| student_id_S7690 |        2.74379 |
| student_id_S7691 |       -4.25159 |
| student_id_S7692 |       -1.00576 |
| student_id_S7693 |        8.5347  |
| student_id_S7694 |        2.3786  |
| student_id_S7696 |       -9.64029 |
| student_id_S7697 |       -3.21024 |
| student_id_S7698 |        6.54356 |
| student_id_S7699 |       16.0588  |

---

### Blocco 636 (Feature 6351 - 6360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S77   |     -13.8564   |
| student_id_S770  |       7.66738  |
| student_id_S7700 |      -0.895289 |
| student_id_S7701 |      -1.2097   |
| student_id_S7702 |     -12.7207   |
| student_id_S7704 |       6.05805  |
| student_id_S7705 |     -18.3023   |
| student_id_S7706 |     -10.4948   |
| student_id_S7707 |       4.65751  |
| student_id_S7708 |      -3.57869  |

---

### Blocco 637 (Feature 6361 - 6370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7709 |      -1.84845  |
| student_id_S771  |      -0.777117 |
| student_id_S7710 |       4.84322  |
| student_id_S7711 |       0.888065 |
| student_id_S7712 |       6.94019  |
| student_id_S7713 |       7.44352  |
| student_id_S7714 |      -7.9839   |
| student_id_S7715 |       1.92195  |
| student_id_S7716 |       5.60159  |
| student_id_S7717 |      -5.31058  |

---

### Blocco 638 (Feature 6371 - 6380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7718 |       -4.34312 |
| student_id_S7719 |       -4.46417 |
| student_id_S772  |      -11.0599  |
| student_id_S7720 |       14.5937  |
| student_id_S7721 |      -11.7485  |
| student_id_S7723 |        2.58143 |
| student_id_S7725 |       -7.71794 |
| student_id_S7726 |       -6.09193 |
| student_id_S7727 |       -5.3443  |
| student_id_S7729 |       -4.97618 |

---

### Blocco 639 (Feature 6381 - 6390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S773  |       3.3075   |
| student_id_S7730 |       1.95296  |
| student_id_S7731 |      -4.41882  |
| student_id_S7732 |      11.1218   |
| student_id_S7733 |      -2.76292  |
| student_id_S7734 |       0.713634 |
| student_id_S7735 |       1.91447  |
| student_id_S7736 |      -1.21408  |
| student_id_S7737 |       4.90715  |
| student_id_S7738 |       8.54413  |

---

### Blocco 640 (Feature 6391 - 6400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7739 |       0.150943 |
| student_id_S774  |      -6.80541  |
| student_id_S7740 |     -11.3308   |
| student_id_S7741 |       7.93998  |
| student_id_S7742 |       2.64674  |
| student_id_S7743 |      -3.01069  |
| student_id_S7744 |      -4.10141  |
| student_id_S7745 |       8.86535  |
| student_id_S7746 |      13.7857   |
| student_id_S7747 |      -3.52163  |

---

### Blocco 641 (Feature 6401 - 6410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7749 |       -2.04991 |
| student_id_S775  |       -9.3915  |
| student_id_S7750 |        8.32272 |
| student_id_S7751 |        6.82435 |
| student_id_S7752 |        3.5426  |
| student_id_S7753 |        9.91848 |
| student_id_S7754 |       -2.07033 |
| student_id_S7755 |        7.18111 |
| student_id_S7756 |        2.68294 |
| student_id_S7757 |        3.47662 |

---

### Blocco 642 (Feature 6411 - 6420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7758 |      -1.27069  |
| student_id_S7759 |      -1.16961  |
| student_id_S776  |      -8.50607  |
| student_id_S7760 |      -4.36115  |
| student_id_S7761 |      -5.94253  |
| student_id_S7762 |       6.87154  |
| student_id_S7763 |       7.70311  |
| student_id_S7764 |       0.720317 |
| student_id_S7765 |      -5.15335  |
| student_id_S7766 |      -3.23855  |

---

### Blocco 643 (Feature 6421 - 6430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7767 |        4.44967 |
| student_id_S7768 |       -4.1148  |
| student_id_S7769 |        2.47606 |
| student_id_S777  |        7.86536 |
| student_id_S7772 |        6.2598  |
| student_id_S7774 |       -8.74674 |
| student_id_S7775 |      -11.5248  |
| student_id_S7776 |        6.05824 |
| student_id_S7777 |       -7.06104 |
| student_id_S7778 |       10.6095  |

---

### Blocco 644 (Feature 6431 - 6440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7779 |       4.52463  |
| student_id_S778  |       0.57163  |
| student_id_S7780 |       5.48298  |
| student_id_S7781 |      -7.24477  |
| student_id_S7784 |       3.31758  |
| student_id_S7785 |      -5.54196  |
| student_id_S7786 |       6.66575  |
| student_id_S7787 |       6.5059   |
| student_id_S7788 |       0.885826 |
| student_id_S7789 |     -11.8045   |

---

### Blocco 645 (Feature 6441 - 6450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S779  |     11.4115    |
| student_id_S7790 |     -0.557122  |
| student_id_S7791 |     -5.96309   |
| student_id_S7792 |     -0.0743011 |
| student_id_S7793 |     -1.50164   |
| student_id_S7794 |      2.88946   |
| student_id_S7795 |     -0.502124  |
| student_id_S7797 |     -1.21893   |
| student_id_S7798 |    -15.2457    |
| student_id_S7799 |     -0.407777  |

---

### Blocco 646 (Feature 6451 - 6460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S78   |     -10.249    |
| student_id_S780  |      -7.08887  |
| student_id_S7800 |      -0.733311 |
| student_id_S7801 |      -6.21063  |
| student_id_S7803 |      -2.75631  |
| student_id_S7804 |       1.97411  |
| student_id_S7805 |       5.45416  |
| student_id_S7806 |       4.1941   |
| student_id_S7807 |      12.0278   |
| student_id_S7809 |       9.10756  |

---

### Blocco 647 (Feature 6461 - 6470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7811 |      -0.158256 |
| student_id_S7813 |       2.42195  |
| student_id_S7814 |       0.089039 |
| student_id_S7815 |      15.0396   |
| student_id_S7816 |       4.49033  |
| student_id_S7818 |      -3.59439  |
| student_id_S7819 |       8.38956  |
| student_id_S782  |      -1.63844  |
| student_id_S7820 |      -0.656038 |
| student_id_S7821 |       3.13649  |

---

### Blocco 648 (Feature 6471 - 6480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7822 |        6.34171 |
| student_id_S7823 |       -2.13409 |
| student_id_S7824 |        1.26406 |
| student_id_S7825 |       -8.60492 |
| student_id_S7827 |       10.1695  |
| student_id_S7828 |       -3.50019 |
| student_id_S7829 |       13.2796  |
| student_id_S783  |      -10.6158  |
| student_id_S7830 |       10.7187  |
| student_id_S7831 |        4.14609 |

---

### Blocco 649 (Feature 6481 - 6490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7833 |      -6.50174  |
| student_id_S7834 |       7.82607  |
| student_id_S7835 |      -1.80844  |
| student_id_S7836 |      -0.609899 |
| student_id_S7837 |      14.6198   |
| student_id_S7838 |      -5.52331  |
| student_id_S7839 |      -5.77128  |
| student_id_S784  |       1.13585  |
| student_id_S7840 |      12.164    |
| student_id_S7841 |       8.04433  |

---

### Blocco 650 (Feature 6491 - 6500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7842 |        6.97615 |
| student_id_S7843 |        5.13431 |
| student_id_S7844 |       13.952   |
| student_id_S7845 |       -0.71012 |
| student_id_S7846 |        2.67005 |
| student_id_S7847 |       11.854   |
| student_id_S7848 |       -1.4019  |
| student_id_S7849 |        1.54107 |
| student_id_S785  |       10.079   |
| student_id_S7850 |        9.03079 |

---

### Blocco 651 (Feature 6501 - 6510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7851 |      10.3208   |
| student_id_S7852 |       1.38321  |
| student_id_S7853 |      -9.55359  |
| student_id_S7854 |      -2.15448  |
| student_id_S7855 |      -0.31396  |
| student_id_S7856 |      -0.293492 |
| student_id_S7857 |      -9.08188  |
| student_id_S7858 |      -0.567816 |
| student_id_S7859 |      -1.67865  |
| student_id_S786  |      -5.00696  |

---

### Blocco 652 (Feature 6511 - 6520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7861 |        4.02527 |
| student_id_S7862 |        5.40533 |
| student_id_S7864 |       -8.81248 |
| student_id_S7865 |      -10.887   |
| student_id_S7867 |       -2.37069 |
| student_id_S7868 |       11.6226  |
| student_id_S7869 |        8.78162 |
| student_id_S787  |        2.46745 |
| student_id_S7870 |       13.1497  |
| student_id_S7871 |        2.92802 |

---

### Blocco 653 (Feature 6521 - 6530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7872 |       0.244128 |
| student_id_S7874 |      10.8279   |
| student_id_S7875 |       3.04077  |
| student_id_S7876 |      14.8733   |
| student_id_S7877 |      -9.94983  |
| student_id_S7878 |      -2.81597  |
| student_id_S7879 |       7.58669  |
| student_id_S7880 |     -15.9441   |
| student_id_S7881 |     -11.3516   |
| student_id_S7882 |       5.3102   |

---

### Blocco 654 (Feature 6531 - 6540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7883 |        6.40902 |
| student_id_S7884 |      -13.8772  |
| student_id_S7885 |       11.9688  |
| student_id_S7886 |       -3.27354 |
| student_id_S7887 |        7.84881 |
| student_id_S7888 |       -5.47919 |
| student_id_S7889 |        7.30665 |
| student_id_S789  |        5.28067 |
| student_id_S7890 |       14.8183  |
| student_id_S7891 |        1.41464 |

---

### Blocco 655 (Feature 6541 - 6550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7892 |      10.1814   |
| student_id_S7893 |       4.70292  |
| student_id_S7894 |      13.482    |
| student_id_S7895 |      10.7551   |
| student_id_S7896 |       9.99677  |
| student_id_S7897 |     -16.236    |
| student_id_S7899 |       4.22658  |
| student_id_S79   |       0.255119 |
| student_id_S790  |       0.57328  |
| student_id_S7901 |      -3.77968  |

---

### Blocco 656 (Feature 6551 - 6560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7902 |       -9.67731 |
| student_id_S7903 |        7.76319 |
| student_id_S7904 |        3.19371 |
| student_id_S7905 |        3.60577 |
| student_id_S7906 |        4.16647 |
| student_id_S7908 |       -5.79069 |
| student_id_S7909 |        6.05831 |
| student_id_S791  |       -5.6056  |
| student_id_S7911 |       -2.08129 |
| student_id_S7912 |      -15.7997  |

---

### Blocco 657 (Feature 6561 - 6570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7913 |      -0.707025 |
| student_id_S7914 |      -2.5609   |
| student_id_S7915 |      -7.29274  |
| student_id_S7916 |      -8.15124  |
| student_id_S7917 |       3.70995  |
| student_id_S7918 |      -3.78041  |
| student_id_S7919 |      -0.303083 |
| student_id_S792  |       8.79146  |
| student_id_S7920 |      -2.38669  |
| student_id_S7921 |     -13.7135   |

---

### Blocco 658 (Feature 6571 - 6580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7922 |      -7.84584  |
| student_id_S7923 |       2.4434   |
| student_id_S7925 |       4.46909  |
| student_id_S7926 |      -3.58643  |
| student_id_S7927 |       2.96422  |
| student_id_S7928 |      -0.122927 |
| student_id_S7929 |      -5.95865  |
| student_id_S793  |      -4.32248  |
| student_id_S7930 |       8.27702  |
| student_id_S7931 |       0.328927 |

---

### Blocco 659 (Feature 6581 - 6590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7932 |       7.71071  |
| student_id_S7933 |     -10.4772   |
| student_id_S7935 |      -8.62793  |
| student_id_S7936 |       0.509483 |
| student_id_S7937 |       2.16817  |
| student_id_S7939 |       1.80888  |
| student_id_S794  |      -1.85965  |
| student_id_S7940 |      -9.04957  |
| student_id_S7941 |      -2.1133   |
| student_id_S7942 |      -4.27158  |

---

### Blocco 660 (Feature 6591 - 6600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7943 |      -4.29712  |
| student_id_S7945 |       0.932098 |
| student_id_S7946 |      11.0991   |
| student_id_S7947 |      -0.834698 |
| student_id_S7948 |       0.181064 |
| student_id_S7949 |      -7.81554  |
| student_id_S795  |       2.83002  |
| student_id_S7950 |       2.15726  |
| student_id_S7952 |      -2.92494  |
| student_id_S7953 |       2.86856  |

---

### Blocco 661 (Feature 6601 - 6610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7954 |      9.67481   |
| student_id_S7955 |     -0.0920494 |
| student_id_S7956 |     -6.57705   |
| student_id_S7957 |     -3.66166   |
| student_id_S7958 |     -9.24748   |
| student_id_S7959 |     -1.7696    |
| student_id_S796  |     -5.95205   |
| student_id_S7960 |     -6.62326   |
| student_id_S7962 |     -6.74875   |
| student_id_S7963 |     -4.02385   |

---

### Blocco 662 (Feature 6611 - 6620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7964 |       9.51513  |
| student_id_S7965 |      -8.97993  |
| student_id_S7967 |       5.09648  |
| student_id_S7969 |       0.582015 |
| student_id_S797  |     -11.6567   |
| student_id_S7970 |      -2.92533  |
| student_id_S7971 |      16.6784   |
| student_id_S7972 |     -13.2914   |
| student_id_S7973 |       7.05743  |
| student_id_S7974 |     -14.1631   |

---

### Blocco 663 (Feature 6621 - 6630)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7975 |     -10.4602   |
| student_id_S7977 |      -7.12282  |
| student_id_S7978 |      -2.76646  |
| student_id_S7979 |       9.40769  |
| student_id_S798  |       8.55418  |
| student_id_S7980 |      -1.68571  |
| student_id_S7981 |       0.830937 |
| student_id_S7982 |      -4.42948  |
| student_id_S7983 |     -12.8153   |
| student_id_S7984 |       7.07295  |

---

### Blocco 664 (Feature 6631 - 6640)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7985 |       0.412915 |
| student_id_S7986 |       0.424613 |
| student_id_S7987 |       3.30421  |
| student_id_S7988 |       0.558    |
| student_id_S7989 |       4.29392  |
| student_id_S7990 |      -6.07157  |
| student_id_S7992 |       0.323725 |
| student_id_S7994 |       2.42279  |
| student_id_S7995 |      14.5586   |
| student_id_S7996 |       3.87081  |

---

### Blocco 665 (Feature 6641 - 6650)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S7997 |        4.85295 |
| student_id_S7999 |       11.1803  |
| student_id_S8    |        5.49593 |
| student_id_S80   |        4.50886 |
| student_id_S800  |       -4.50401 |
| student_id_S8000 |       12.0874  |
| student_id_S8001 |       11.9618  |
| student_id_S8002 |       -8.63778 |
| student_id_S8004 |       -5.30973 |
| student_id_S8005 |       -1.8441  |

---

### Blocco 666 (Feature 6651 - 6660)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8006 |      -5.89398  |
| student_id_S8008 |      -0.729838 |
| student_id_S8009 |       3.34837  |
| student_id_S801  |      -1.354    |
| student_id_S8010 |       5.48049  |
| student_id_S8011 |       1.26073  |
| student_id_S8012 |       3.96718  |
| student_id_S8013 |      12.2191   |
| student_id_S8015 |      -9.26034  |
| student_id_S8016 |       3.6534   |

---

### Blocco 667 (Feature 6661 - 6670)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8017 |        6.78106 |
| student_id_S8018 |       -5.43023 |
| student_id_S8019 |       10.4688  |
| student_id_S802  |       -6.20457 |
| student_id_S8020 |       -4.26286 |
| student_id_S8021 |      -15.0184  |
| student_id_S8022 |       -6.95817 |
| student_id_S8023 |        1.10267 |
| student_id_S8024 |       -2.44878 |
| student_id_S8025 |        6.42608 |

---

### Blocco 668 (Feature 6671 - 6680)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8026 |      -0.392647 |
| student_id_S8027 |      10.4359   |
| student_id_S8029 |       4.69956  |
| student_id_S803  |      -3.56792  |
| student_id_S8030 |      -3.70566  |
| student_id_S8031 |       2.89618  |
| student_id_S8032 |       0.613109 |
| student_id_S8033 |      -2.97675  |
| student_id_S8034 |      -1.87875  |
| student_id_S8036 |      -1.65794  |

---

### Blocco 669 (Feature 6681 - 6690)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8037 |     -11.3804   |
| student_id_S8039 |      -1.12268  |
| student_id_S804  |      -8.60254  |
| student_id_S8040 |      -0.976591 |
| student_id_S8041 |       4.39882  |
| student_id_S8042 |       1.06367  |
| student_id_S8043 |      -0.47674  |
| student_id_S8044 |      -5.71297  |
| student_id_S8045 |       0.271728 |
| student_id_S8046 |      -4.11015  |

---

### Blocco 670 (Feature 6691 - 6700)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8047 |        3.8185  |
| student_id_S8049 |        2.53067 |
| student_id_S805  |        9.38342 |
| student_id_S8050 |       -6.1703  |
| student_id_S8051 |        4.50565 |
| student_id_S8052 |        4.84635 |
| student_id_S8053 |      -14.7864  |
| student_id_S8054 |       -9.37819 |
| student_id_S8055 |       -7.02035 |
| student_id_S8056 |       -2.10667 |

---

### Blocco 671 (Feature 6701 - 6710)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8057 |        5.53518 |
| student_id_S8059 |      -10.4339  |
| student_id_S806  |       13.1644  |
| student_id_S8060 |       -6.54117 |
| student_id_S8061 |      -11.6073  |
| student_id_S8062 |       -8.72046 |
| student_id_S8063 |      -13.0133  |
| student_id_S8065 |        9.52838 |
| student_id_S8067 |       14.8249  |
| student_id_S8068 |       -3.43435 |

---

### Blocco 672 (Feature 6711 - 6720)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8069 |      -3.36949  |
| student_id_S807  |      -5.75374  |
| student_id_S8070 |      -3.65494  |
| student_id_S8071 |       2.29923  |
| student_id_S8072 |      -0.25871  |
| student_id_S8073 |       5.14285  |
| student_id_S8074 |      -6.53333  |
| student_id_S8075 |      -4.48381  |
| student_id_S8076 |       3.14602  |
| student_id_S8077 |       0.378437 |

---

### Blocco 673 (Feature 6721 - 6730)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8078 |        6.59559 |
| student_id_S8079 |       -4.18496 |
| student_id_S808  |       -4.6188  |
| student_id_S8080 |       10.6922  |
| student_id_S8081 |       -4.32599 |
| student_id_S8082 |       -4.83415 |
| student_id_S8084 |        5.24807 |
| student_id_S8085 |       -8.82473 |
| student_id_S8086 |       -3.36614 |
| student_id_S8087 |       -5.06695 |

---

### Blocco 674 (Feature 6731 - 6740)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8088 |      15.6272   |
| student_id_S8089 |       2.45648  |
| student_id_S809  |       9.76662  |
| student_id_S8090 |       5.12644  |
| student_id_S8091 |      -0.781516 |
| student_id_S8092 |      12.9869   |
| student_id_S8093 |       7.09622  |
| student_id_S8094 |      -9.7856   |
| student_id_S8095 |       3.0997   |
| student_id_S8096 |       1.52847  |

---

### Blocco 675 (Feature 6741 - 6750)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8097 |        3.23818 |
| student_id_S8099 |       -6.41201 |
| student_id_S8100 |       -3.66674 |
| student_id_S8101 |        7.42623 |
| student_id_S8102 |       14.8053  |
| student_id_S8103 |       -3.23971 |
| student_id_S8104 |       -4.48313 |
| student_id_S8105 |       15.6741  |
| student_id_S8106 |        5.30737 |
| student_id_S8107 |        9.98195 |

---

### Blocco 676 (Feature 6751 - 6760)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8108 |      -1.57616  |
| student_id_S811  |      -0.512711 |
| student_id_S8110 |      -0.533393 |
| student_id_S8112 |      -1.47816  |
| student_id_S8113 |     -11.495    |
| student_id_S8114 |      -6.19692  |
| student_id_S8115 |      -0.246875 |
| student_id_S8116 |      -9.69206  |
| student_id_S8118 |       0.284526 |
| student_id_S8119 |      -3.25015  |

---

### Blocco 677 (Feature 6761 - 6770)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S812  |       -1.17972 |
| student_id_S8120 |        3.39613 |
| student_id_S8122 |       -6.44542 |
| student_id_S8123 |        4.1227  |
| student_id_S8125 |      -16.1387  |
| student_id_S8126 |       -9.38808 |
| student_id_S8127 |       -8.04308 |
| student_id_S8128 |       -4.65271 |
| student_id_S8129 |       11.7135  |
| student_id_S813  |        4.00757 |

---

### Blocco 678 (Feature 6771 - 6780)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8132 |       4.27901  |
| student_id_S8133 |       0.361745 |
| student_id_S8134 |      -2.96623  |
| student_id_S8135 |      -4.72461  |
| student_id_S8136 |      12.8795   |
| student_id_S8137 |       0.672874 |
| student_id_S8138 |       3.33427  |
| student_id_S8139 |      16.4747   |
| student_id_S814  |      -0.44633  |
| student_id_S8140 |      -3.83168  |

---

### Blocco 679 (Feature 6781 - 6790)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8141 |      -1.67891  |
| student_id_S8142 |      -0.280267 |
| student_id_S8144 |      -2.66129  |
| student_id_S8145 |       0.812716 |
| student_id_S8146 |      -5.36012  |
| student_id_S8147 |      -9.42458  |
| student_id_S8148 |      -2.09397  |
| student_id_S8149 |      -2.24059  |
| student_id_S815  |      -2.79845  |
| student_id_S8151 |      -1.18765  |

---

### Blocco 680 (Feature 6791 - 6800)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8152 |      -1.14202  |
| student_id_S8154 |      -2.87539  |
| student_id_S8156 |      -0.379754 |
| student_id_S8157 |       7.506    |
| student_id_S8159 |       9.45577  |
| student_id_S816  |      -6.80466  |
| student_id_S8160 |       7.28896  |
| student_id_S8161 |      13.6807   |
| student_id_S8162 |      -7.08998  |
| student_id_S8163 |      -4.04407  |

---

### Blocco 681 (Feature 6801 - 6810)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8164 |       6.67229  |
| student_id_S8165 |       7.15482  |
| student_id_S8166 |      -4.89193  |
| student_id_S8168 |      17.6948   |
| student_id_S8169 |      -4.59251  |
| student_id_S817  |      -4.12033  |
| student_id_S8170 |      -7.81837  |
| student_id_S8171 |      11.1676   |
| student_id_S8172 |       0.854026 |
| student_id_S8173 |       3.59093  |

---

### Blocco 682 (Feature 6811 - 6820)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8174 |        1.51302 |
| student_id_S8175 |       -4.11742 |
| student_id_S8176 |        6.21648 |
| student_id_S8178 |        3.2489  |
| student_id_S8179 |       -4.48942 |
| student_id_S818  |        2.02806 |
| student_id_S8180 |       -6.29905 |
| student_id_S8181 |       -4.13778 |
| student_id_S8182 |       -8.19218 |
| student_id_S8183 |       -5.91846 |

---

### Blocco 683 (Feature 6821 - 6830)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8184 |       -4.32261 |
| student_id_S8185 |        6.84089 |
| student_id_S8186 |       10.2233  |
| student_id_S8187 |        9.16948 |
| student_id_S8188 |        2.70822 |
| student_id_S8189 |        4.68545 |
| student_id_S819  |        6.04968 |
| student_id_S8190 |      -13.696   |
| student_id_S8191 |       16.2158  |
| student_id_S8192 |        7.20558 |

---

### Blocco 684 (Feature 6831 - 6840)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8193 |       3.5385   |
| student_id_S8194 |      -1.79055  |
| student_id_S8195 |      -0.281815 |
| student_id_S8196 |      -7.59663  |
| student_id_S8197 |      -7.56536  |
| student_id_S8199 |     -14.1296   |
| student_id_S82   |     -14.1346   |
| student_id_S820  |     -10.3877   |
| student_id_S8200 |      -6.28573  |
| student_id_S8201 |      -2.48755  |

---

### Blocco 685 (Feature 6841 - 6850)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8204 |      -7.93838  |
| student_id_S8205 |       5.34916  |
| student_id_S8206 |       7.61275  |
| student_id_S8207 |       8.90501  |
| student_id_S821  |       8.09018  |
| student_id_S8211 |       1.09182  |
| student_id_S8212 |      -0.753705 |
| student_id_S8213 |      -0.206796 |
| student_id_S8214 |      -5.11964  |
| student_id_S8215 |       5.21662  |

---

### Blocco 686 (Feature 6851 - 6860)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8216 |     -10.7999   |
| student_id_S8217 |       7.11081  |
| student_id_S8219 |      -8.22881  |
| student_id_S822  |       2.44612  |
| student_id_S8220 |       2.53131  |
| student_id_S8221 |      -1.2252   |
| student_id_S8222 |       3.55358  |
| student_id_S8223 |      -3.03761  |
| student_id_S8224 |       0.600534 |
| student_id_S8225 |       5.39439  |

---

### Blocco 687 (Feature 6861 - 6870)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8226 |       7.50899  |
| student_id_S8227 |       1.52463  |
| student_id_S8229 |      10.772    |
| student_id_S823  |       3.40726  |
| student_id_S8230 |      -3.83738  |
| student_id_S8231 |      -9.61894  |
| student_id_S8232 |       0.772508 |
| student_id_S8233 |       8.61419  |
| student_id_S8234 |      -1.4661   |
| student_id_S8235 |       5.68861  |

---

### Blocco 688 (Feature 6871 - 6880)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8237 |      -1.41087  |
| student_id_S8238 |      -0.412683 |
| student_id_S824  |       5.92827  |
| student_id_S8240 |       6.71085  |
| student_id_S8241 |      -8.43987  |
| student_id_S8242 |      -3.98325  |
| student_id_S8243 |       7.70791  |
| student_id_S8244 |      -2.11382  |
| student_id_S8245 |       3.54846  |
| student_id_S8246 |       7.68802  |

---

### Blocco 689 (Feature 6881 - 6890)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8247 |     5.12468    |
| student_id_S8248 |     2.27508    |
| student_id_S8249 |    -8.55145    |
| student_id_S825  |    11.1663     |
| student_id_S8250 |    -0.00305395 |
| student_id_S8251 |    -6.95885    |
| student_id_S8252 |    -7.22978    |
| student_id_S8253 |    11.028      |
| student_id_S8254 |    -4.97765    |
| student_id_S8255 |     1.78661    |

---

### Blocco 690 (Feature 6891 - 6900)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8256 |        1.60048 |
| student_id_S8257 |        1.51949 |
| student_id_S8259 |        8.39055 |
| student_id_S826  |        3.23917 |
| student_id_S8260 |       -1.04272 |
| student_id_S8261 |      -14.6981  |
| student_id_S8263 |       -6.45853 |
| student_id_S8264 |       -4.48078 |
| student_id_S8265 |      -13.7321  |
| student_id_S8266 |      -12.4972  |

---

### Blocco 691 (Feature 6901 - 6910)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8268 |      13.7615   |
| student_id_S8269 |      -1.99755  |
| student_id_S827  |      -9.6848   |
| student_id_S8270 |      -2.01636  |
| student_id_S8271 |      -2.9895   |
| student_id_S8272 |      -5.94727  |
| student_id_S8273 |      -0.253864 |
| student_id_S8274 |      -1.86337  |
| student_id_S8275 |      -4.01424  |
| student_id_S8276 |       9.39523  |

---

### Blocco 692 (Feature 6911 - 6920)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8277 |        2.95722 |
| student_id_S8278 |       11.1109  |
| student_id_S8279 |       13.3007  |
| student_id_S828  |        1.80315 |
| student_id_S8281 |        1.76361 |
| student_id_S8282 |       -7.45246 |
| student_id_S8283 |       13.0456  |
| student_id_S8284 |       12.8145  |
| student_id_S8285 |       -4.6798  |
| student_id_S8286 |       10.4053  |

---

### Blocco 693 (Feature 6921 - 6930)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8287 |      -0.227708 |
| student_id_S8288 |       5.05485  |
| student_id_S8289 |      -3.13121  |
| student_id_S829  |       7.73738  |
| student_id_S8290 |      -1.43882  |
| student_id_S8291 |      -2.93768  |
| student_id_S8292 |      -8.36523  |
| student_id_S8293 |       9.5155   |
| student_id_S8294 |      -5.22208  |
| student_id_S8295 |      -3.79692  |

---

### Blocco 694 (Feature 6931 - 6940)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8296 |       -3.65604 |
| student_id_S8297 |       -6.70436 |
| student_id_S8298 |       -8.62704 |
| student_id_S83   |        8.54562 |
| student_id_S8300 |        5.31264 |
| student_id_S8302 |       -2.21997 |
| student_id_S8303 |       -8.37328 |
| student_id_S8304 |        5.76223 |
| student_id_S8305 |       -4.47509 |
| student_id_S8306 |       -8.58066 |

---

### Blocco 695 (Feature 6941 - 6950)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8307 |      -4.24243  |
| student_id_S8308 |       8.06014  |
| student_id_S8309 |      -4.0016   |
| student_id_S831  |       1.86742  |
| student_id_S8311 |       1.63964  |
| student_id_S8312 |     -10.828    |
| student_id_S8313 |      -5.30411  |
| student_id_S8314 |       2.88323  |
| student_id_S8315 |       3.03532  |
| student_id_S8316 |      -0.761094 |

---

### Blocco 696 (Feature 6951 - 6960)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8317 |      -5.51747  |
| student_id_S8318 |      -0.957541 |
| student_id_S8319 |       3.20592  |
| student_id_S832  |       8.18113  |
| student_id_S8320 |       1.77228  |
| student_id_S8321 |       7.29867  |
| student_id_S8323 |     -10.8717   |
| student_id_S8324 |       7.54774  |
| student_id_S8326 |      -5.27302  |
| student_id_S8327 |      -8.32664  |

---

### Blocco 697 (Feature 6961 - 6970)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8328 |        4.5398  |
| student_id_S833  |       -8.49206 |
| student_id_S8330 |        4.0265  |
| student_id_S8331 |        1.47717 |
| student_id_S8332 |       -9.82726 |
| student_id_S8333 |        1.41114 |
| student_id_S8334 |       -6.30861 |
| student_id_S8335 |       -9.97501 |
| student_id_S8336 |      -16.475   |
| student_id_S8338 |       -7.12891 |

---

### Blocco 698 (Feature 6971 - 6980)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8339 |        4.94021 |
| student_id_S834  |       -2.23389 |
| student_id_S8340 |        6.57996 |
| student_id_S8341 |        2.26925 |
| student_id_S8343 |      -13.9132  |
| student_id_S8344 |        7.65464 |
| student_id_S8345 |        1.93546 |
| student_id_S8346 |        3.54792 |
| student_id_S8348 |       10.2314  |
| student_id_S8349 |        1.40034 |

---

### Blocco 699 (Feature 6981 - 6990)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S835  |       4.64748  |
| student_id_S8350 |       4.31044  |
| student_id_S8352 |      -3.38183  |
| student_id_S8353 |      -5.60116  |
| student_id_S8354 |      -0.109887 |
| student_id_S8355 |      -5.97341  |
| student_id_S8356 |       7.29116  |
| student_id_S8358 |       3.95742  |
| student_id_S8359 |       9.27674  |
| student_id_S836  |      -3.06023  |

---

### Blocco 700 (Feature 6991 - 7000)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8360 |      12.5909   |
| student_id_S8362 |      -4.44242  |
| student_id_S8363 |      -9.51844  |
| student_id_S8366 |      -1.5354   |
| student_id_S8367 |       0.790424 |
| student_id_S8368 |       5.47274  |
| student_id_S8369 |      -2.09691  |
| student_id_S837  |       3.05491  |
| student_id_S8371 |      -5.76581  |
| student_id_S8373 |       1.28194  |

---

### Blocco 701 (Feature 7001 - 7010)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8374 |      9.68377   |
| student_id_S8375 |      7.13095   |
| student_id_S8377 |     -1.86398   |
| student_id_S8378 |     10.381     |
| student_id_S8379 |     -5.76388   |
| student_id_S838  |      9.05015   |
| student_id_S8380 |      0.0987503 |
| student_id_S8381 |     -7.89935   |
| student_id_S8382 |      5.67106   |
| student_id_S8383 |      3.68226   |

---

### Blocco 702 (Feature 7011 - 7020)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8384 |       -2.74708 |
| student_id_S8385 |      -11.5709  |
| student_id_S8386 |       -2.30176 |
| student_id_S8387 |       -5.58251 |
| student_id_S8388 |       -7.02005 |
| student_id_S8389 |       10.5018  |
| student_id_S839  |      -11.2101  |
| student_id_S8390 |       11.509   |
| student_id_S8391 |        3.70915 |
| student_id_S8392 |       10.6556  |

---

### Blocco 703 (Feature 7021 - 7030)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8393 |     -7.4198    |
| student_id_S8394 |     -0.744639  |
| student_id_S8395 |     -3.41192   |
| student_id_S8396 |    -13.5445    |
| student_id_S8397 |     -1.33552   |
| student_id_S8398 |      5.83288   |
| student_id_S8399 |     -2.28216   |
| student_id_S84   |      0.0649266 |
| student_id_S840  |     -6.8129    |
| student_id_S8400 |     -1.50564   |

---

### Blocco 704 (Feature 7031 - 7040)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8401 |      2.96359   |
| student_id_S8403 |     -3.63922   |
| student_id_S8404 |     -5.91786   |
| student_id_S8405 |      4.10315   |
| student_id_S8406 |      3.40824   |
| student_id_S8407 |     -0.522269  |
| student_id_S8408 |     -5.1537    |
| student_id_S8409 |     -1.02635   |
| student_id_S841  |     -5.92962   |
| student_id_S8410 |      0.0361023 |

---

### Blocco 705 (Feature 7041 - 7050)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8412 |       8.87681  |
| student_id_S8413 |       2.29659  |
| student_id_S8414 |       3.68067  |
| student_id_S8415 |       3.14262  |
| student_id_S8416 |      -6.68829  |
| student_id_S8417 |       3.39015  |
| student_id_S8418 |      -5.26457  |
| student_id_S8419 |       9.97408  |
| student_id_S842  |      -0.354404 |
| student_id_S8420 |       7.17472  |

---

### Blocco 706 (Feature 7051 - 7060)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8422 |      -5.33319  |
| student_id_S8423 |      -3.0075   |
| student_id_S8424 |      -5.0257   |
| student_id_S8425 |       8.07679  |
| student_id_S8426 |       5.66293  |
| student_id_S8427 |       1.16866  |
| student_id_S8428 |       0.309688 |
| student_id_S8429 |      10.4932   |
| student_id_S843  |      -8.33194  |
| student_id_S8430 |       2.61379  |

---

### Blocco 707 (Feature 7061 - 7070)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8432 |      -0.584497 |
| student_id_S8434 |      -2.09078  |
| student_id_S8435 |       3.84891  |
| student_id_S8436 |      13.8523   |
| student_id_S8437 |      10.147    |
| student_id_S8438 |      -4.69429  |
| student_id_S8439 |     -10.5206   |
| student_id_S8440 |      -8.3611   |
| student_id_S8441 |      -3.68472  |
| student_id_S8442 |      -3.19671  |

---

### Blocco 708 (Feature 7071 - 7080)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8443 |      -4.51896  |
| student_id_S8444 |      -9.13184  |
| student_id_S8445 |       7.021    |
| student_id_S8447 |       5.964    |
| student_id_S8448 |       3.67511  |
| student_id_S845  |      -2.29116  |
| student_id_S8450 |     -12.4857   |
| student_id_S8452 |      11.0805   |
| student_id_S8453 |      -9.31784  |
| student_id_S8454 |      -0.516898 |

---

### Blocco 709 (Feature 7081 - 7090)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8455 |        5.37419 |
| student_id_S8456 |        6.89723 |
| student_id_S8457 |       12.8942  |
| student_id_S8458 |       -9.55691 |
| student_id_S8459 |        5.00594 |
| student_id_S8460 |       -8.76524 |
| student_id_S8461 |       -3.85769 |
| student_id_S8462 |        7.56785 |
| student_id_S8463 |        7.08722 |
| student_id_S8464 |       13.3214  |

---

### Blocco 710 (Feature 7091 - 7100)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8465 |      13.2689   |
| student_id_S8466 |       2.99634  |
| student_id_S8467 |      -1.61552  |
| student_id_S8468 |       8.57295  |
| student_id_S8469 |       0.388571 |
| student_id_S847  |      -3.76864  |
| student_id_S8470 |       5.51359  |
| student_id_S8471 |       4.53069  |
| student_id_S8472 |       2.49046  |
| student_id_S8473 |       4.80889  |

---

### Blocco 711 (Feature 7101 - 7110)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8474 |        3.95144 |
| student_id_S8475 |        7.71825 |
| student_id_S8476 |       -2.16535 |
| student_id_S8477 |      -13.7536  |
| student_id_S8478 |        7.11357 |
| student_id_S8479 |       -5.74247 |
| student_id_S848  |        1.77126 |
| student_id_S8481 |       -1.91173 |
| student_id_S8482 |       -1.484   |
| student_id_S8483 |        8.59489 |

---

### Blocco 712 (Feature 7111 - 7120)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8485 |       1.33588  |
| student_id_S8486 |      -1.98936  |
| student_id_S8487 |      -1.49378  |
| student_id_S8488 |      -2.64277  |
| student_id_S8489 |      -6.88514  |
| student_id_S849  |       0.270449 |
| student_id_S8490 |      -9.97564  |
| student_id_S8492 |       4.95216  |
| student_id_S8493 |       2.29853  |
| student_id_S8494 |      -6.22206  |

---

### Blocco 713 (Feature 7121 - 7130)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8495 |        7.78725 |
| student_id_S8496 |        5.29636 |
| student_id_S8498 |       -7.00121 |
| student_id_S8499 |       -4.87515 |
| student_id_S85   |      -10.231   |
| student_id_S850  |        4.91411 |
| student_id_S8500 |       13.5083  |
| student_id_S8501 |       -1.5002  |
| student_id_S8502 |       -6.61727 |
| student_id_S8503 |      -11.6105  |

---

### Blocco 714 (Feature 7131 - 7140)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8504 |      -7.80895  |
| student_id_S8505 |      -2.6506   |
| student_id_S8506 |      -3.39107  |
| student_id_S8507 |      -0.207781 |
| student_id_S8508 |     -10.3977   |
| student_id_S8509 |       7.54428  |
| student_id_S851  |       4.18911  |
| student_id_S8510 |       9.03517  |
| student_id_S8511 |       3.16799  |
| student_id_S8512 |      -1.29087  |

---

### Blocco 715 (Feature 7141 - 7150)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8513 |       2.40527  |
| student_id_S8514 |      13.2453   |
| student_id_S8515 |       5.80649  |
| student_id_S8516 |      -6.57612  |
| student_id_S8517 |      -5.18503  |
| student_id_S8518 |       0.115421 |
| student_id_S8519 |      11.972    |
| student_id_S852  |       6.16034  |
| student_id_S8521 |       2.73173  |
| student_id_S8523 |      -1.14691  |

---

### Blocco 716 (Feature 7151 - 7160)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8524 |      -8.61936  |
| student_id_S8525 |     -11.4456   |
| student_id_S8526 |      -6.86418  |
| student_id_S8527 |       2.20137  |
| student_id_S8528 |     -12.5039   |
| student_id_S8529 |      -4.04081  |
| student_id_S8530 |       7.48051  |
| student_id_S8531 |       7.83925  |
| student_id_S8533 |      -2.44991  |
| student_id_S8534 |      -0.381841 |

---

### Blocco 717 (Feature 7161 - 7170)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8535 |       -2.91598 |
| student_id_S8536 |       -4.89934 |
| student_id_S8537 |       11.3085  |
| student_id_S8538 |        5.44623 |
| student_id_S8539 |       -5.29686 |
| student_id_S854  |       -5.17331 |
| student_id_S8540 |       -6.39845 |
| student_id_S8541 |        7.33157 |
| student_id_S8543 |       -3.09958 |
| student_id_S8546 |        5.35682 |

---

### Blocco 718 (Feature 7171 - 7180)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8547 |      10.8088   |
| student_id_S855  |      -8.39577  |
| student_id_S8550 |      -0.205483 |
| student_id_S8552 |      -5.98353  |
| student_id_S8553 |       4.3253   |
| student_id_S8554 |      -0.391679 |
| student_id_S8555 |     -12.0885   |
| student_id_S8556 |      -2.14531  |
| student_id_S8557 |     -10.4722   |
| student_id_S8558 |       5.35163  |

---

### Blocco 719 (Feature 7181 - 7190)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S856  |      17.188    |
| student_id_S8560 |      -2.20799  |
| student_id_S8561 |       1.5977   |
| student_id_S8562 |      -0.343437 |
| student_id_S8564 |       3.31932  |
| student_id_S8565 |      -2.25881  |
| student_id_S8566 |       3.82686  |
| student_id_S8567 |       5.83971  |
| student_id_S8568 |       8.39395  |
| student_id_S8569 |       6.65747  |

---

### Blocco 720 (Feature 7191 - 7200)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S857  |      16.6383   |
| student_id_S8570 |      10.446    |
| student_id_S8571 |      -6.40082  |
| student_id_S8572 |       8.55517  |
| student_id_S8573 |      -5.82731  |
| student_id_S8574 |       9.26234  |
| student_id_S8575 |       1.52459  |
| student_id_S8576 |       0.864994 |
| student_id_S8577 |       4.08344  |
| student_id_S8578 |      -4.63753  |

---

### Blocco 721 (Feature 7201 - 7210)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8579 |       -1.57228 |
| student_id_S858  |       11.9176  |
| student_id_S8580 |      -16.3127  |
| student_id_S8581 |        4.3318  |
| student_id_S8582 |       -4.48676 |
| student_id_S8583 |       -4.1915  |
| student_id_S8584 |        1.38529 |
| student_id_S8585 |       -5.38668 |
| student_id_S8586 |       -6.02182 |
| student_id_S8587 |        9.56211 |

---

### Blocco 722 (Feature 7211 - 7220)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8589 |     -13.1186   |
| student_id_S859  |       5.50411  |
| student_id_S8590 |       3.01923  |
| student_id_S8591 |       3.01092  |
| student_id_S8592 |      -4.38763  |
| student_id_S8593 |       3.60231  |
| student_id_S8594 |      13.8264   |
| student_id_S8595 |       1.42705  |
| student_id_S8596 |      -1.7557   |
| student_id_S8597 |       0.965032 |

---

### Blocco 723 (Feature 7221 - 7230)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8598 |       5.85088  |
| student_id_S8599 |       4.80021  |
| student_id_S86   |       1.76889  |
| student_id_S860  |      13.9119   |
| student_id_S8600 |      -1.09056  |
| student_id_S8601 |       0.840776 |
| student_id_S8602 |      -5.68346  |
| student_id_S8603 |      -4.47809  |
| student_id_S8604 |      -3.83955  |
| student_id_S8605 |      -4.55387  |

---

### Blocco 724 (Feature 7231 - 7240)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8606 |      3.70405   |
| student_id_S8607 |      3.81688   |
| student_id_S8608 |     -1.08993   |
| student_id_S861  |      4.24221   |
| student_id_S8611 |     -0.0587389 |
| student_id_S8612 |     -6.61626   |
| student_id_S8613 |     -9.97692   |
| student_id_S8614 |      3.15825   |
| student_id_S8615 |      7.23264   |
| student_id_S8616 |      6.43693   |

---

### Blocco 725 (Feature 7241 - 7250)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8617 |        2.46393 |
| student_id_S8619 |        7.84303 |
| student_id_S862  |        1.86    |
| student_id_S8620 |        3.74993 |
| student_id_S8621 |        9.30853 |
| student_id_S8622 |       -6.44663 |
| student_id_S8623 |       -2.46184 |
| student_id_S8625 |        6.06736 |
| student_id_S8626 |       -7.85375 |
| student_id_S8627 |        3.57382 |

---

### Blocco 726 (Feature 7251 - 7260)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8628 |       4.58847  |
| student_id_S8629 |       0.812151 |
| student_id_S863  |      -6.97491  |
| student_id_S8630 |      10.0456   |
| student_id_S8632 |       9.78593  |
| student_id_S8633 |      16.2161   |
| student_id_S8634 |      -6.62854  |
| student_id_S8635 |       3.41298  |
| student_id_S8636 |      -3.57964  |
| student_id_S8637 |      -6.56698  |

---

### Blocco 727 (Feature 7261 - 7270)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8638 |       6.4861   |
| student_id_S8639 |       3.5208   |
| student_id_S8640 |       8.90401  |
| student_id_S8642 |       9.51116  |
| student_id_S8643 |      -2.98971  |
| student_id_S8644 |       1.83036  |
| student_id_S8645 |      -6.86158  |
| student_id_S8646 |      -7.57632  |
| student_id_S8647 |       0.224913 |
| student_id_S8649 |       9.45102  |

---

### Blocco 728 (Feature 7271 - 7280)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S865  |      -0.561733 |
| student_id_S8650 |      -6.59293  |
| student_id_S8651 |       8.13089  |
| student_id_S8652 |      -7.03497  |
| student_id_S8653 |       6.51622  |
| student_id_S8654 |       4.23386  |
| student_id_S8655 |      10.027    |
| student_id_S8656 |      -1.67174  |
| student_id_S8657 |       2.28334  |
| student_id_S8658 |      15.6867   |

---

### Blocco 729 (Feature 7281 - 7290)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8659 |      0.122875  |
| student_id_S866  |    -11.8774    |
| student_id_S8660 |     -8.71745   |
| student_id_S8661 |      0.0666374 |
| student_id_S8662 |      0.401429  |
| student_id_S8663 |      0.377561  |
| student_id_S8664 |     -4.95201   |
| student_id_S8665 |     -0.948172  |
| student_id_S8666 |    -14.3236    |
| student_id_S8667 |      5.18877   |

---

### Blocco 730 (Feature 7291 - 7300)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8668 |      -0.178212 |
| student_id_S8669 |       5.10733  |
| student_id_S867  |       1.74585  |
| student_id_S8670 |      -9.39157  |
| student_id_S8671 |      12.8851   |
| student_id_S8672 |       8.4877   |
| student_id_S8674 |     -10.05     |
| student_id_S8675 |      -2.86774  |
| student_id_S8676 |      -6.57436  |
| student_id_S8677 |      -3.17369  |

---

### Blocco 731 (Feature 7301 - 7310)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8679 |      -5.37696  |
| student_id_S868  |      13.6795   |
| student_id_S8680 |      -3.12444  |
| student_id_S8681 |       9.5625   |
| student_id_S8683 |       9.54176  |
| student_id_S8684 |     -12.4969   |
| student_id_S8686 |       8.66896  |
| student_id_S8687 |      -4.4584   |
| student_id_S8688 |       4.33121  |
| student_id_S8689 |       0.312012 |

---

### Blocco 732 (Feature 7311 - 7320)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S869  |       8.01225  |
| student_id_S8690 |     -12.0949   |
| student_id_S8691 |       0.582906 |
| student_id_S8692 |       3.68982  |
| student_id_S8693 |       3.60906  |
| student_id_S8694 |       5.57104  |
| student_id_S8695 |       2.74452  |
| student_id_S8697 |      -9.16692  |
| student_id_S8698 |       1.53877  |
| student_id_S87   |      12.0945   |

---

### Blocco 733 (Feature 7321 - 7330)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S870  |      -4.20459  |
| student_id_S8700 |       6.81284  |
| student_id_S8701 |      -2.89836  |
| student_id_S8702 |       7.73871  |
| student_id_S8704 |      -1.28621  |
| student_id_S8705 |      -0.554875 |
| student_id_S8706 |       6.03914  |
| student_id_S8707 |       7.85741  |
| student_id_S8708 |       0.159765 |
| student_id_S8709 |      -2.85088  |

---

### Blocco 734 (Feature 7331 - 7340)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S871  |      6.63044   |
| student_id_S8710 |      0.280273  |
| student_id_S8713 |     -2.24415   |
| student_id_S8714 |      7.44012   |
| student_id_S8715 |      3.7602    |
| student_id_S8716 |     -9.94023   |
| student_id_S8717 |      1.70609   |
| student_id_S8718 |     -3.56037   |
| student_id_S8719 |     -2.37      |
| student_id_S872  |      0.0270851 |

---

### Blocco 735 (Feature 7341 - 7350)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8720 |        5.12248 |
| student_id_S8721 |       11.7466  |
| student_id_S8722 |      -10.4901  |
| student_id_S8724 |       -2.23142 |
| student_id_S8725 |        1.28133 |
| student_id_S8726 |       -9.09824 |
| student_id_S8727 |       -5.92211 |
| student_id_S8728 |       -1.49436 |
| student_id_S8729 |       11.7571  |
| student_id_S873  |        9.36381 |

---

### Blocco 736 (Feature 7351 - 7360)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8730 |      -9.81507  |
| student_id_S8731 |      -6.25361  |
| student_id_S8732 |      -9.96632  |
| student_id_S8733 |      -0.917755 |
| student_id_S8734 |     -11.7485   |
| student_id_S8735 |     -11.5422   |
| student_id_S8736 |       5.47911  |
| student_id_S8737 |      12.5846   |
| student_id_S8738 |       1.85946  |
| student_id_S8739 |      -2.11811  |

---

### Blocco 737 (Feature 7361 - 7370)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S874  |      -7.10257  |
| student_id_S8740 |       0.154003 |
| student_id_S8741 |      -1.42226  |
| student_id_S8743 |       0.937264 |
| student_id_S8744 |      -0.260331 |
| student_id_S8745 |      -3.38011  |
| student_id_S8746 |       1.05702  |
| student_id_S8747 |       1.38728  |
| student_id_S8748 |       2.03001  |
| student_id_S8749 |       0.216309 |

---

### Blocco 738 (Feature 7371 - 7380)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S875  |        9.99699 |
| student_id_S8750 |       -1.29808 |
| student_id_S8751 |       -5.54264 |
| student_id_S8752 |      -11.4075  |
| student_id_S8753 |        5.23451 |
| student_id_S8754 |        6.23239 |
| student_id_S8755 |      -13.6459  |
| student_id_S8756 |        6.92226 |
| student_id_S8757 |       -4.78069 |
| student_id_S8758 |        7.09805 |

---

### Blocco 739 (Feature 7381 - 7390)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S876  |       0.768362 |
| student_id_S8760 |      -9.42613  |
| student_id_S8761 |      -8.81091  |
| student_id_S8762 |      -6.10646  |
| student_id_S8763 |      -8.54997  |
| student_id_S8764 |     -13.01     |
| student_id_S8765 |       5.43466  |
| student_id_S8766 |      -9.73959  |
| student_id_S8767 |      -2.22458  |
| student_id_S8768 |      16.7018   |

---

### Blocco 740 (Feature 7391 - 7400)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8769 |     -5.82863   |
| student_id_S877  |      4.74377   |
| student_id_S8770 |      1.64372   |
| student_id_S8771 |     -5.18148   |
| student_id_S8772 |    -11.1142    |
| student_id_S8773 |      3.96603   |
| student_id_S8775 |     -3.62815   |
| student_id_S8776 |      2.37655   |
| student_id_S8778 |      3.60448   |
| student_id_S8779 |      0.0437404 |

---

### Blocco 741 (Feature 7401 - 7410)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8780 |       1.78655  |
| student_id_S8782 |       5.53412  |
| student_id_S8783 |       9.42724  |
| student_id_S8784 |      -2.44586  |
| student_id_S8785 |       9.31343  |
| student_id_S8786 |      -4.36059  |
| student_id_S8787 |      -1.48451  |
| student_id_S8788 |      -0.816509 |
| student_id_S8789 |      -1.70193  |
| student_id_S879  |       1.56417  |

---

### Blocco 742 (Feature 7411 - 7420)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8791 |       -5.24324 |
| student_id_S8792 |        7.4669  |
| student_id_S8793 |       -1.08066 |
| student_id_S8794 |       -8.45344 |
| student_id_S8795 |       10.8377  |
| student_id_S8798 |       -6.64358 |
| student_id_S8799 |       -5.54495 |
| student_id_S88   |       -6.1885  |
| student_id_S880  |       -6.23585 |
| student_id_S8800 |       -1.25678 |

---

### Blocco 743 (Feature 7421 - 7430)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8801 |       -3.58607 |
| student_id_S8802 |       -5.86332 |
| student_id_S8803 |       17.5231  |
| student_id_S8804 |       -3.15759 |
| student_id_S8805 |       -2.88163 |
| student_id_S8806 |      -17.7721  |
| student_id_S8807 |        8.92635 |
| student_id_S8808 |       -7.1111  |
| student_id_S8809 |        1.31347 |
| student_id_S881  |       -1.66641 |

---

### Blocco 744 (Feature 7431 - 7440)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8810 |        9.56126 |
| student_id_S8812 |       -1.34802 |
| student_id_S8813 |        3.00813 |
| student_id_S8814 |        6.44266 |
| student_id_S8815 |       11.9281  |
| student_id_S8816 |        2.975   |
| student_id_S8817 |       -4.96538 |
| student_id_S8818 |       -3.5722  |
| student_id_S8819 |       -0.03888 |
| student_id_S882  |        6.34696 |

---

### Blocco 745 (Feature 7441 - 7450)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8821 |    -1.28075    |
| student_id_S8822 |    -6.96071    |
| student_id_S8823 |     5.6988     |
| student_id_S8824 |    -6.39357    |
| student_id_S8827 |    10.0645     |
| student_id_S8828 |    -3.64288    |
| student_id_S8829 |    11.9531     |
| student_id_S883  |    -0.00189695 |
| student_id_S8830 |     7.57217    |
| student_id_S8831 |    -1.80285    |

---

### Blocco 746 (Feature 7451 - 7460)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8834 |       -2.18151 |
| student_id_S8835 |        1.13299 |
| student_id_S8836 |       -6.72502 |
| student_id_S8838 |       -2.01295 |
| student_id_S8839 |      -11.9036  |
| student_id_S884  |        1.92666 |
| student_id_S8841 |       -1.98149 |
| student_id_S8842 |        5.31938 |
| student_id_S8843 |        5.24473 |
| student_id_S8844 |       11.576   |

---

### Blocco 747 (Feature 7461 - 7470)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8845 |       -3.48273 |
| student_id_S8846 |      -10.983   |
| student_id_S8847 |        7.33424 |
| student_id_S8848 |       -0.45493 |
| student_id_S8849 |       -5.68983 |
| student_id_S885  |       12.2675  |
| student_id_S8850 |        2.62229 |
| student_id_S8851 |       -7.22534 |
| student_id_S8852 |       -2.86949 |
| student_id_S8853 |       -6.47781 |

---

### Blocco 748 (Feature 7471 - 7480)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8854 |      -0.456551 |
| student_id_S8855 |      -3.86351  |
| student_id_S8856 |      -0.303681 |
| student_id_S8857 |      -2.89147  |
| student_id_S8858 |       3.49366  |
| student_id_S8859 |       0.603074 |
| student_id_S886  |       2.01104  |
| student_id_S8860 |       1.45968  |
| student_id_S8861 |      -9.5989   |
| student_id_S8862 |      -1.34337  |

---

### Blocco 749 (Feature 7481 - 7490)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8863 |       1.55951  |
| student_id_S8865 |       7.65616  |
| student_id_S8866 |       4.80555  |
| student_id_S8867 |       3.24384  |
| student_id_S8868 |       5.1298   |
| student_id_S8869 |      -3.81382  |
| student_id_S887  |      -8.46608  |
| student_id_S8871 |      -3.1585   |
| student_id_S8872 |      -0.732043 |
| student_id_S8873 |      -9.22077  |

---

### Blocco 750 (Feature 7491 - 7500)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8874 |       2.2732   |
| student_id_S8875 |      -7.69248  |
| student_id_S8876 |      12.5389   |
| student_id_S8877 |      -2.94014  |
| student_id_S8878 |       2.26244  |
| student_id_S8879 |      -8.83749  |
| student_id_S888  |      -7.20705  |
| student_id_S8881 |       8.31531  |
| student_id_S8883 |       0.172988 |
| student_id_S8884 |       5.59042  |

---

### Blocco 751 (Feature 7501 - 7510)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8885 |      11.902    |
| student_id_S8886 |      -0.571916 |
| student_id_S8887 |      -0.848373 |
| student_id_S8888 |       3.09456  |
| student_id_S8889 |      -4.11166  |
| student_id_S8890 |      -6.68739  |
| student_id_S8892 |      -4.93045  |
| student_id_S8893 |       6.09175  |
| student_id_S8894 |      12.3687   |
| student_id_S8895 |     -11.0247   |

---

### Blocco 752 (Feature 7511 - 7520)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8896 |       2.57457  |
| student_id_S8897 |      10.443    |
| student_id_S8899 |      -8.42701  |
| student_id_S89   |      -6.75997  |
| student_id_S890  |      -5.00511  |
| student_id_S8900 |       2.98758  |
| student_id_S8901 |       0.469335 |
| student_id_S8902 |       5.95832  |
| student_id_S8903 |       6.40395  |
| student_id_S8904 |       6.17566  |

---

### Blocco 753 (Feature 7521 - 7530)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8905 |      11.0964   |
| student_id_S8906 |       1.61081  |
| student_id_S8907 |       2.92739  |
| student_id_S8908 |      -2.93745  |
| student_id_S8909 |       0.495743 |
| student_id_S891  |      -5.3075   |
| student_id_S8910 |      -2.719    |
| student_id_S8911 |     -14.4434   |
| student_id_S8912 |      -3.22542  |
| student_id_S8913 |     -15.3451   |

---

### Blocco 754 (Feature 7531 - 7540)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8914 |       -2.10603 |
| student_id_S8915 |        2.11479 |
| student_id_S8916 |      -12.874   |
| student_id_S8917 |       12.1208  |
| student_id_S8918 |        3.52881 |
| student_id_S8919 |       -2.8872  |
| student_id_S892  |        3.5203  |
| student_id_S8920 |        7.2395  |
| student_id_S8921 |       -5.1902  |
| student_id_S8924 |       -1.48766 |

---

### Blocco 755 (Feature 7541 - 7550)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8925 |       10.6395  |
| student_id_S8926 |       -6.72976 |
| student_id_S8927 |        5.00678 |
| student_id_S8928 |       14.9935  |
| student_id_S8929 |       -6.73334 |
| student_id_S893  |        7.71049 |
| student_id_S8930 |       -5.69128 |
| student_id_S8931 |       -1.97029 |
| student_id_S8932 |       -4.32233 |
| student_id_S8933 |        7.50838 |

---

### Blocco 756 (Feature 7551 - 7560)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8934 |       0.201992 |
| student_id_S8935 |      12.3798   |
| student_id_S8936 |       1.04524  |
| student_id_S8938 |      -6.38722  |
| student_id_S8939 |      -8.28352  |
| student_id_S894  |      -4.53701  |
| student_id_S8941 |       3.94488  |
| student_id_S8942 |      10.379    |
| student_id_S8943 |      -9.37587  |
| student_id_S8944 |      10.0073   |

---

### Blocco 757 (Feature 7561 - 7570)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8945 |      3.084     |
| student_id_S8946 |     -0.0596542 |
| student_id_S8948 |      2.80474   |
| student_id_S8949 |      1.84837   |
| student_id_S895  |      3.66632   |
| student_id_S8950 |      7.01536   |
| student_id_S8951 |     -3.50487   |
| student_id_S8952 |      1.20551   |
| student_id_S8953 |      8.4753    |
| student_id_S8954 |    -10.7685    |

---

### Blocco 758 (Feature 7571 - 7580)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8955 |     -2.84756   |
| student_id_S8956 |     -4.58464   |
| student_id_S8957 |    -15.2113    |
| student_id_S8958 |      5.49604   |
| student_id_S8959 |      6.50361   |
| student_id_S896  |     -2.84783   |
| student_id_S8960 |     -5.21851   |
| student_id_S8961 |      0.55335   |
| student_id_S8962 |     14.0821    |
| student_id_S8963 |     -0.0341225 |

---

### Blocco 759 (Feature 7581 - 7590)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8964 |       -4.42478 |
| student_id_S8965 |        1.03931 |
| student_id_S8966 |        8.90782 |
| student_id_S8967 |       -5.68608 |
| student_id_S8969 |       10.5096  |
| student_id_S897  |      -14.561   |
| student_id_S8970 |        2.66494 |
| student_id_S8971 |       -2.53996 |
| student_id_S8972 |       10.59    |
| student_id_S8973 |        4.72936 |

---

### Blocco 760 (Feature 7591 - 7600)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8975 |     -8.64453   |
| student_id_S8976 |     -0.605897  |
| student_id_S8977 |     12.6416    |
| student_id_S8978 |      7.81512   |
| student_id_S8979 |     -0.0687477 |
| student_id_S898  |      8.55565   |
| student_id_S8980 |     -8.03474   |
| student_id_S8981 |     -2.84307   |
| student_id_S8983 |     -2.49528   |
| student_id_S8984 |      2.127     |

---

### Blocco 761 (Feature 7601 - 7610)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8985 |       1.94353  |
| student_id_S8987 |       0.501872 |
| student_id_S8988 |      -1.37652  |
| student_id_S8989 |       0.32011  |
| student_id_S899  |       0.270799 |
| student_id_S8990 |      13.6624   |
| student_id_S8992 |       7.46115  |
| student_id_S8994 |       5.94155  |
| student_id_S8995 |      -3.96289  |
| student_id_S8996 |     -10.7268   |

---

### Blocco 762 (Feature 7611 - 7620)
| Feature          |   Coefficiente |
|:-----------------|---------------:|
| student_id_S8997 |       3.69     |
| student_id_S8998 |      -4.91799  |
| student_id_S8999 |      14.6345   |
| student_id_S9    |      -3.00296  |
| student_id_S90   |      -5.88277  |
| student_id_S900  |       4.32927  |
| student_id_S902  |       0.532259 |
| student_id_S904  |      -5.52819  |
| student_id_S905  |       8.97335  |
| student_id_S906  |      -8.62609  |

---

### Blocco 763 (Feature 7621 - 7630)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S908 |      -8.36959  |
| student_id_S909 |       1.99617  |
| student_id_S91  |      -0.863176 |
| student_id_S910 |       3.81788  |
| student_id_S911 |       2.53217  |
| student_id_S912 |     -10.6625   |
| student_id_S913 |      -3.89723  |
| student_id_S914 |       2.518    |
| student_id_S915 |      -9.72131  |
| student_id_S916 |      -3.87628  |

---

### Blocco 764 (Feature 7631 - 7640)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S917 |       -5.20578 |
| student_id_S918 |      -11.8791  |
| student_id_S919 |       -6.41706 |
| student_id_S92  |       -5.37753 |
| student_id_S920 |       -1.05366 |
| student_id_S921 |        8.1683  |
| student_id_S922 |       -5.74413 |
| student_id_S923 |       -4.55436 |
| student_id_S924 |       -5.1369  |
| student_id_S925 |        3.06332 |

---

### Blocco 765 (Feature 7641 - 7650)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S926 |      -0.581687 |
| student_id_S928 |      -3.52874  |
| student_id_S929 |     -15.0719   |
| student_id_S93  |       4.53636  |
| student_id_S930 |      -3.96399  |
| student_id_S931 |      -8.82961  |
| student_id_S932 |      -1.68868  |
| student_id_S933 |      -0.314741 |
| student_id_S935 |      -0.9586   |
| student_id_S937 |       4.92159  |

---

### Blocco 766 (Feature 7651 - 7660)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S938 |      12.4516   |
| student_id_S939 |       4.02908  |
| student_id_S94  |     -10.1177   |
| student_id_S940 |       7.10597  |
| student_id_S941 |      -0.782735 |
| student_id_S942 |      -5.33463  |
| student_id_S943 |      -0.36905  |
| student_id_S944 |     -10.8083   |
| student_id_S945 |      -5.2282   |
| student_id_S946 |      11.2749   |

---

### Blocco 767 (Feature 7661 - 7670)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S947 |        6.45336 |
| student_id_S948 |       11.9678  |
| student_id_S949 |      -14.5107  |
| student_id_S95  |       -1.24058 |
| student_id_S950 |      -14.2582  |
| student_id_S951 |       -6.71851 |
| student_id_S952 |        7.07073 |
| student_id_S953 |        7.49462 |
| student_id_S954 |       13.2906  |
| student_id_S955 |       -6.70927 |

---

### Blocco 768 (Feature 7671 - 7680)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S956 |     -10.0344   |
| student_id_S957 |      -8.06879  |
| student_id_S958 |      -2.09197  |
| student_id_S959 |      -4.61135  |
| student_id_S96  |       6.17976  |
| student_id_S960 |      -1.88172  |
| student_id_S961 |      -0.162685 |
| student_id_S962 |       6.84458  |
| student_id_S963 |       9.66773  |
| student_id_S964 |      -7.95989  |

---

### Blocco 769 (Feature 7681 - 7690)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S965 |       -8.05052 |
| student_id_S966 |      -10.3669  |
| student_id_S967 |       -6.28102 |
| student_id_S968 |       -3.33421 |
| student_id_S969 |       -3.01327 |
| student_id_S97  |       10.5809  |
| student_id_S970 |       -8.4052  |
| student_id_S971 |        4.45058 |
| student_id_S972 |        8.03184 |
| student_id_S973 |      -12.8226  |

---

### Blocco 770 (Feature 7691 - 7700)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S974 |     -10.4801   |
| student_id_S976 |       9.86105  |
| student_id_S977 |      16.901    |
| student_id_S978 |       1.35302  |
| student_id_S979 |      -0.468825 |
| student_id_S98  |      -2.94501  |
| student_id_S981 |      -5.18799  |
| student_id_S982 |       2.43302  |
| student_id_S983 |      -4.04704  |
| student_id_S984 |       2.7045   |

---

### Blocco 771 (Feature 7701 - 7710)
| Feature         |   Coefficiente |
|:----------------|---------------:|
| student_id_S985 |       9.66073  |
| student_id_S986 |       1.63931  |
| student_id_S987 |      -9.23207  |
| student_id_S988 |       2.8519   |
| student_id_S989 |     -10.6312   |
| student_id_S99  |       1.41123  |
| student_id_S990 |       4.76078  |
| student_id_S992 |       0.111182 |
| student_id_S993 |      11.2277   |
| student_id_S994 |      -0.377845 |

---

### Blocco 772 (Feature 7711 - 7720)
| Feature           |   Coefficiente |
|:------------------|---------------:|
| student_id_S995   |     -6.96293   |
| student_id_S996   |    -10.5152    |
| student_id_S997   |      0.853838  |
| student_id_S998   |     -2.19427   |
| student_id_S999   |     -1.30706   |
| branch_Civil      |     -2.54483   |
| branch_ECE        |      0.265475  |
| branch_EEE        |      0.491506  |
| branch_IT         |      0.251342  |
| branch_Mechanical |     -0.0252741 |

---

### Blocco 773 (Feature 7721 - 7726)
| Feature                    |   Coefficiente |
|:---------------------------|---------------:|
| company_type_Mid-size      |     -16.8032   |
| company_type_Startup       |     -30.8147   |
| company_type_Top Tech      |      23.3889   |
| job_role_Data Scientist    |       0.231612 |
| job_role_Software Engineer |      -1.67145  |
| job_role_Web Developer     |       0.112784 |

---

## 3. Spiegabilità e SHAP Values
Le metriche di spiegabilità locale e globale sono state calcolate tramite campionamento di 100 record (`X100`).
Per l'interpretazione visiva dell'impatto delle variabili (es. `cgpa`), fare riferimento ai grafici Partial Dependence e Beeswarm generati dall'esecuzione principale dello script.
