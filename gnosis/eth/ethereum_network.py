from enum import Enum, unique


class EthereumNetworkNotSupported(Exception):
    pass


@unique
class EthereumNetwork(Enum):
    """
    Use https://chainlist.org/ as a reference
    """

    UNKNOWN = -1
    OLYMPIC = 0
    MAINNET = 1
    EXPANSE_NETWORK = 2
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    ETHEREUM_CLASSIC_TESTNET_KOTTI = 6
    THAICHAIN = 7
    UBIQ = 8
    UBIQ_NETWORK_TESTNET = 9
    OPTIMISM = 10
    METADIUM_MAINNET = 11
    METADIUM_TESTNET = 12
    DIODE_TESTNET_STAGING = 13
    FLARE_MAINNET = 14
    DIODE_PRENET = 15
    FLARE_TESTNET_COSTON = 16
    THAICHAIN_2_0_THAIFI = 17
    THUNDERCORE_TESTNET = 18
    SONGBIRD_CANARY_NETWORK = 19
    ELASTOS_SMART_CHAIN = 20
    ELASTOS_SMART_CHAIN_TESTNET = 21
    ELA_DID_SIDECHAIN_MAINNET = 22
    ELA_DID_SIDECHAIN_TESTNET = 23
    KARDIACHAIN_MAINNET = 24
    CRONOS_MAINNET_BETA = 25
    GENESIS_L1_TESTNET = 26
    SHIBACHAIN = 27
    BOBA_NETWORK_RINKEBY_TESTNET = 28
    GENESIS_L1 = 29
    RSK_MAINNET = 30
    RSK_TESTNET = 31
    GOODDATA_TESTNET = 32
    GOODDATA_MAINNET = 33
    DITHEREUM_TESTNET = 34
    TBWG_CHAIN = 35
    DXCHAIN_MAINNET = 36
    SEEDCOIN_NETWORK = 37
    VALORBIT = 38
    UNICORN_ULTRA_TESTNET = 39
    TELOS_EVM_MAINNET = 40
    TELOS_EVM_TESTNET = 41
    KOVAN = 42
    DARWINIA_PANGOLIN_TESTNET = 43
    DARWINIA_CRAB_NETWORK = 44
    DARWINIA_PANGORO_TESTNET = 45
    DARWINIA_NETWORK = 46
    ENNOTHEM_MAINNET_PROTEROZOIC = 48
    ENNOTHEM_TESTNET_PIONEER = 49
    XINFIN_XDC_NETWORK = 50
    XDC_APOTHEM_NETWORK = 51
    COINEX_SMART_CHAIN_MAINNET = 52
    COINEX_SMART_CHAIN_TESTNET = 53
    OPENPIECE_MAINNET = 54
    ZYX_MAINNET = 55
    BINANCE_SMART_CHAIN_MAINNET = 56
    SYSCOIN_MAINNET = 57
    ONTOLOGY_MAINNET = 58
    EOS_MAINNET = 59
    GOCHAIN = 60
    ETHEREUM_CLASSIC_MAINNET = 61
    ETHEREUM_CLASSIC_TESTNET_MORDEN = 62
    ETHEREUM_CLASSIC_TESTNET_MORDOR = 63
    ELLAISM = 64
    OKEXCHAIN_TESTNET = 65
    OKXCHAIN_MAINNET = 66
    DBCHAIN_TESTNET = 67
    SOTERONE_MAINNET = 68
    OPTIMISM_KOVAN = 69
    HOO_SMART_CHAIN = 70
    CONFLUX_ESPACE_TESTNET = 71
    DXCHAIN_TESTNET = 72
    FNCY = 73
    IDCHAIN_MAINNET = 74
    DECIMAL_SMART_CHAIN_MAINNET = 75
    MIX = 76
    POA_NETWORK_SOKOL = 77
    PRIMUSCHAIN_MAINNET = 78
    ZENITH_MAINNET = 79
    GENECHAIN = 80
    ZENITH_TESTNET_VILNIUS = 81
    METER_MAINNET = 82
    METER_TESTNET = 83
    GATECHAIN_TESTNET = 85
    GATECHAIN_MAINNET = 86
    NOVA_NETWORK = 87
    TOMOCHAIN = 88
    TOMOCHAIN_TESTNET = 89
    GARIZON_STAGE0 = 90
    GARIZON_STAGE1 = 91
    GARIZON_STAGE2 = 92
    GARIZON_STAGE3 = 93
    CRYPTOKYLIN_TESTNET = 95
    NEXT_SMART_CHAIN = 96
    BINANCE_SMART_CHAIN_TESTNET = 97
    POA_NETWORK_CORE = 99
    GNOSIS = 100
    ETHERINC = 101
    WEB3GAMES_TESTNET = 102
    KAIBA_LIGHTNING_CHAIN_TESTNET = 104
    WEB3GAMES_DEVNET = 105
    VELAS_EVM_MAINNET = 106
    NEBULA_TESTNET = 107
    THUNDERCORE_MAINNET = 108
    PROTON_TESTNET = 110
    ETHERLITE_CHAIN = 111
    DEHVO = 113
    FLARE_TESTNET_COSTON2 = 114
    DEBANK_TESTNET = 115
    DEBANK_MAINNET = 116
    FUSE_MAINNET = 122
    FUSE_SPARKNET = 123
    DECENTRALIZED_WEB_MAINNET = 124
    OYCHAIN_TESTNET = 125
    OYCHAIN_MAINNET = 126
    FACTORY_127_MAINNET = 127
    HUOBI_ECO_CHAIN_MAINNET = 128
    ALYX_CHAIN_TESTNET = 135
    POLYGON = 137
    OPENPIECE_TESTNET = 141
    DAX_CHAIN = 142
    PHI_NETWORK_V2 = 144
    TENET_TESTNET = 155
    ARMONIA_EVA_CHAIN_MAINNET = 160
    ARMONIA_EVA_CHAIN_TESTNET = 161
    LIGHTSTREAMS_TESTNET = 162
    LIGHTSTREAMS_MAINNET = 163
    AIOZ_NETWORK = 168
    HOO_SMART_CHAIN_TESTNET = 170
    LATAM_BLOCKCHAIN_RESIL_TESTNET = 172
    AME_CHAIN_MAINNET = 180
    SEELE_MAINNET = 186
    BMC_MAINNET = 188
    BMC_TESTNET = 189
    CRYPTO_EMERGENCY = 193
    BITTORRENT_CHAIN_MAINNET = 199
    ARBITRUM_ON_XDAI = 200
    MOAC_TESTNET = 201
    FREIGHT_TRUST_NETWORK = 211
    MAP_MAKALU = 212
    SIRIUSNET_V2 = 217
    SOTERONE_MAINNET_OLD = 218
    PERMISSION = 222
    LACHAIN_MAINNET = 225
    LACHAIN_TESTNET = 226
    ENERGY_WEB_CHAIN = 246
    OASYS_MAINNET = 248
    FANTOM_OPERA = 250
    HUOBI_ECO_CHAIN_TESTNET = 256
    SETHEUM = 258
    SUR_BLOCKCHAIN_NETWORK = 262
    HIGH_PERFORMANCE_BLOCKCHAIN = 269
    ZKSYNC_ALPHA_TESTNET = 280
    BOBA_NETWORK = 288
    OPTIMISM_ON_GNOSIS = 300
    BOBAOPERA = 301
    OMAX_MAINNET = 311
    FILECOIN_MAINNET = 314
    KCC_MAINNET = 321
    KCC_TESTNET = 322
    ZKSYNC_V2 = 324
    WEB3Q_MAINNET = 333
    DFK_CHAIN_TEST = 335
    SHIDEN = 336
    CRONOS_TESTNET = 338
    THETA_MAINNET = 361
    THETA_SAPPHIRE_TESTNET = 363
    THETA_AMBER_TESTNET = 364
    THETA_TESTNET = 365
    PULSECHAIN_MAINNET = 369
    LISINSKI = 385
    HYPERONCHAIN_TESTNET = 400
    SX_NETWORK_MAINNET = 416
    OPTIMISM_GOERLI_TESTNET = 420
    ZEETH_CHAIN = 427
    RUPAYA = 499
    CAMINO_C_CHAIN = 500
    COLUMBUS_TEST_NETWORK = 501
    DOUBLE_A_CHAIN_MAINNET = 512
    DOUBLE_A_CHAIN_TESTNET = 513
    GEAR_ZERO_NETWORK_MAINNET = 516
    XT_SMART_CHAIN_MAINNET = 520
    FIRECHAIN_MAINNET = 529
    F_XCORE_MAINNET_NETWORK = 530
    CANDLE = 534
    VELA1_CHAIN_MAINNET = 555
    TAO_NETWORK = 558
    DOGECHAIN_TESTNET = 568
    METIS_STARDUST_TESTNET = 588
    ASTAR = 592
    ACALA_MANDALA_TESTNET = 595
    KARURA_NETWORK_TESTNET = 596
    ACALA_NETWORK_TESTNET = 597
    METIS_GOERLI_TESTNET = 599
    MESHNYAN_TESTNET = 600
    SX_NETWORK_TESTNET = 647
    PIXIE_CHAIN_TESTNET = 666
    KARURA_NETWORK = 686
    STAR_SOCIAL_TESTNET = 700
    BLOCKCHAIN_STATION_MAINNET = 707
    BLOCKCHAIN_STATION_TESTNET = 708
    LYCAN_CHAIN = 721
    VENTION_SMART_CHAIN_TESTNET = 741
    QL1 = 766
    OPENCHAIN_TESTNET = 776
    CHEAPETH = 777
    ACALA_NETWORK = 787
    AEROCHAIN_TESTNET = 788
    LUCID_BLOCKCHAIN = 800
    HAIC = 803
    PORTAL_FANTASY_CHAIN_TEST = 808
    QITMEER = 813
    CALLISTO_MAINNET = 820
    CALLISTO_TESTNET_DEPRECATED = 821
    TARAXA_MAINNET = 841
    TARAXA_TESTNET = 842
    ZEETH_CHAIN_DEV = 859
    FANTASIA_CHAIN_MAINNET = 868
    DEXIT_NETWORK = 877
    AMBROS_CHAIN_MAINNET = 880
    WANCHAIN = 888
    GARIZON_TESTNET_STAGE0 = 900
    GARIZON_TESTNET_STAGE1 = 901
    GARIZON_TESTNET_STAGE2 = 902
    GARIZON_TESTNET_STAGE3 = 903
    PORTAL_FANTASY_CHAIN = 909
    RINIA_TESTNET = 917
    PULSECHAIN_TESTNET = 940
    PULSECHAIN_TESTNET_V2B = 941
    PULSECHAIN_TESTNET_V3 = 942
    MUNODE_TESTNET = 956
    OORT_MAINNET = 970
    OORT_HUYGENS = 971
    OORT_ASCRAEUS = 972
    NEPAL_BLOCKCHAIN_NETWORK = 977
    TOP_MAINNET_EVM = 980
    MEMO_SMART_CHAIN_MAINNET = 985
    TOP_MAINNET = 989
    LUCKY_NETWORK = 998
    WANCHAIN_TESTNET = 999
    GTON_MAINNET = 1000
    KLAYTN_TESTNET_BAOBAB = 1001
    T_EKTA = 1004
    NEWTON_TESTNET = 1007
    EURUS_MAINNET = 1008
    EVRICE_NETWORK = 1010
    NEWTON = 1012
    SAKURA = 1022
    CLOVER_TESTNET = 1023
    CLV_PARACHAIN = 1024
    BITTORRENT_CHAIN_TESTNET = 1028
    CONFLUX_ESPACE = 1030
    PROXY_NETWORK_TESTNET = 1031
    BRONOS_TESTNET = 1038
    BRONOS_MAINNET = 1039
    METIS_ANDROMEDA_MAINNET = 1088
    MOAC_MAINNET = 1099
    POLYGON_ZKEVM = 1101
    WEMIX3_0_MAINNET = 1111
    WEMIX3_0_TESTNET = 1112
    CORE_BLOCKCHAIN_MAINNET = 1116
    DEFICHAIN_EVM_NETWORK_MAINNET = 1130
    DEFICHAIN_EVM_NETWORK_TESTNET = 1131
    MATHCHAIN = 1139
    MATHCHAIN_TESTNET = 1140
    SMART_HOST_TEKNOLOJI_TESTNET = 1177
    IORA_CHAIN = 1197
    EVANESCO_TESTNET = 1201
    WORLD_TRADE_TECHNICAL_CHAIN_MAINNET = 1202
    POPCATEUM_MAINNET = 1213
    ENTERCHAIN_MAINNET = 1214
    EXZO_NETWORK_MAINNET = 1229
    ULTRON_TESTNET = 1230
    ULTRON_MAINNET = 1231
    STEP_NETWORK = 1234
    OM_PLATFORM_MAINNET = 1246
    CIC_CHAIN_TESTNET = 1252
    HALO_MAINNET = 1280
    MOONBEAM = 1284
    MOONRIVER = 1285
    MOONROCK_OLD = 1286
    MOONBASE_ALPHA = 1287
    MOONROCK = 1288
    BOBABEAM = 1294
    BOBABASE_TESTNET = 1297
    DOS_FUJI_SUBNET = 1311
    ALYX_MAINNET = 1314
    AITD_MAINNET = 1319
    AITD_TESTNET = 1320
    GANACHE = 1337
    CIC_CHAIN_MAINNET = 1353
    POLYGON_ZKEVM_TESTNET = 1402
    CTEX_SCAN_BLOCKCHAIN = 1455
    SHERPAX_MAINNET = 1506
    SHERPAX_TESTNET = 1507
    BEAGLE_MESSAGING_CHAIN = 1515
    TENET = 1559
    CATECOIN_CHAIN_MAINNET = 1618
    ATHEIOS = 1620
    BTACHAIN = 1657
    LUDAN_MAINNET = 1688
    ANYTYPE_EVM_CHAIN = 1701
    TBSI_MAINNET = 1707
    TBSI_TESTNET = 1708
    KERLEANO = 1804
    RABBIT_ANALOG_TESTNET_CHAIN = 1807
    CUBE_CHAIN_MAINNET = 1818
    CUBE_CHAIN_TESTNET = 1819
    TESLAFUNDS = 1856
    GITSHOCK_CARTENZ_TESTNET = 1881
    BON_NETWORK = 1898
    ONUS_CHAIN_TESTNET = 1945
    D_CHAIN_MAINNET = 1951
    ATELIER = 1971
    ONUS_CHAIN_MAINNET = 1975
    EURUS_TESTNET = 1984
    ETHERGEM = 1987
    EKTA = 1994
    EDEXA_TESTNET = 1995
    DOGECHAIN_MAINNET = 2000
    MILKOMEDA_C1_MAINNET = 2001
    MILKOMEDA_A1_MAINNET = 2002
    CLOUDWALK_TESTNET = 2008
    CLOUDWALK_MAINNET = 2009
    MAINNETZ_MAINNET = 2016
    PUBLICMINT_DEVNET = 2018
    PUBLICMINT_TESTNET = 2019
    PUBLICMINT_MAINNET = 2020
    EDGEWARE_MAINNET = 2021
    BERESHEET_TESTNET = 2022
    TAYCAN_TESTNET = 2023
    RANGERS_PROTOCOL_MAINNET = 2025
    ORIGINTRAIL_PARACHAIN = 2043
    QUOKKACOIN_MAINNET = 2077
    ECOBALL_MAINNET = 2100
    ECOBALL_TESTNET_ESPUMA = 2101
    EXOSAMA_NETWORK = 2109
    METAPLAYERONE_MAINNET = 2122
    BOSAGORA_MAINNET = 2151
    FINDORA_MAINNET = 2152
    FINDORA_TESTNET = 2153
    FINDORA_FORGE = 2154
    BITCOIN_EVM = 2203
    EVANESCO_MAINNET = 2213
    KAVA_EVM_TESTNET = 2221
    KAVA_EVM = 2222
    VCHAIN_MAINNET = 2223
    BOMB_CHAIN = 2300
    ALTCOINCHAIN = 2330
    BOMB_CHAIN_TESTNET = 2399
    TCG_VERSE_MAINNET = 2400
    XODEX = 2415
    KORTHO_MAINNET = 2559
    TECHPAY_MAINNET = 2569
    POCRNET = 2606
    REDLIGHT_CHAIN_MAINNET = 2611
    EZCHAIN_C_CHAIN_MAINNET = 2612
    EZCHAIN_C_CHAIN_TESTNET = 2613
    BOBA_NETWORK_GOERLI_TESTNET = 2888
    BITYUAN_MAINNET = 2999
    CENNZNET_RATA = 3000
    CENNZNET_NIKAU = 3001
    ORLANDO_CHAIN = 3031
    FILECOIN_HYPERSPACE_TESTNET = 3141
    DEBOUNCE_SUBNET_TESTNET = 3306
    ZCORE_TESTNET = 3331
    WEB3Q_TESTNET = 3333
    WEB3Q_GALILEO = 3334
    PARIBU_NET_MAINNET = 3400
    PARIBU_NET_TESTNET = 3500
    JFIN_CHAIN = 3501
    PANDOPROJECT_MAINNET = 3601
    PANDOPROJECT_TESTNET = 3602
    METACODECHAIN = 3666
    BITTEX_MAINNET = 3690
    EMPIRE_NETWORK = 3693
    CROSSBELL = 3737
    DRAC_NETWORK = 3912
    DYNO_MAINNET = 3966
    DYNO_TESTNET = 3967
    YUANCHAIN_MAINNET = 3999
    FANTOM_TESTNET = 4002
    BOBAOPERA_TESTNET = 4051
    AIOZ_NETWORK_TESTNET = 4102
    PHI_NETWORK_V1 = 4181
    BOBAFUJI_TESTNET = 4328
    HTMLCOIN_MAINNET = 4444
    IOTEX_NETWORK_MAINNET = 4689
    IOTEX_NETWORK_TESTNET = 4690
    VENIDIUM_TESTNET = 4918
    VENIDIUM_MAINNET = 4919
    MANTLE = 5000
    MANTLE_TESTNET = 5001
    TLCHAIN_NETWORK_MAINNET = 5177
    ERASWAP_MAINNET = 5197
    HUMANODE_MAINNET = 5234
    FIRECHAIN_MAINNET_OLD = 5290
    UZMI_NETWORK_MAINNET = 5315
    NAHMII_MAINNET = 5551
    NAHMII_TESTNET = 5553
    CHAIN_VERSE_MAINNET = 5555
    SYSCOIN_TANENBAUM_TESTNET = 5700
    ONTOLOGY_TESTNET = 5851
    WEGOCHAIN_RUBIDIUM_MAINNET = 5869
    TRES_TESTNET = 6065
    TRES_MAINNET = 6066
    PIXIE_CHAIN_MAINNET = 6626
    GOLD_SMART_CHAIN_MAINNET = 6789
    TOMB_CHAIN_MAINNET = 6969
    POLYSMARTCHAIN = 6999
    ZETACHAIN_MAINNET = 7000
    ZETACHAIN_ATHENS_TESTNET = 7001
    ELLA_THE_HEART = 7027
    PLANQ_MAINNET = 7070
    SHYFT_MAINNET = 7341
    CANTO = 7700
    RISE_OF_THE_WARBOTS_TESTNET = 7777
    HAZLOR_TESTNET = 7878
    TELEPORT = 8000
    TELEPORT_TESTNET = 8001
    MDGL_TESTNET = 8029
    SHARDEUM_LIBERTY_1_X = 8080
    SHARDEUM_LIBERTY_2_X = 8081
    STREAMUX_BLOCKCHAIN = 8098
    QITMEER_NETWORK_TESTNET = 8131
    BEONE_CHAIN_TESTNET = 8181
    KLAYTN_MAINNET_CYPRESS = 8217
    BLOCKTON_BLOCKCHAIN = 8272
    KORTHOTEST = 8285
    TOKI_NETWORK = 8654
    TOKI_TESTNET = 8655
    TOOL_GLOBAL_MAINNET = 8723
    TOOL_GLOBAL_TESTNET = 8724
    ALPH_NETWORK = 8738
    TMY_CHAIN = 8768
    UNIQUE = 8880
    QUARTZ_BY_UNIQUE = 8881
    OPAL_TESTNET_BY_UNIQUE = 8882
    SAPPHIRE_BY_UNIQUE = 8883
    XANACHAIN = 8888
    VYVO_SMART_CHAIN = 8889
    MAMMOTH_MAINNET = 8898
    JIBCHAIN_L1 = 8899
    GIANT_MAMMOTH_MAINNET = 8989
    BLOXBERG = 8995
    EVMOS_TESTNET = 9000
    EVMOS = 9001
    BERYLBIT_MAINNET = 9012
    GENESIS_COIN = 9100
    RINIA_TESTNET_OLD = 9170
    RANGERS_PROTOCOL_TESTNET_ROBIN = 9527
    QEASYWEB3_TESTNET = 9528
    OORT_MAINNETDEV = 9700
    BOBA_BNB_TESTNET = 9728
    MAINNETZ_TESTNET = 9768
    MYOWN_TESTNET = 9999
    SMART_BITCOIN_CASH = 10000
    SMART_BITCOIN_CASH_TESTNET = 10001
    GON_CHAIN = 10024
    SJATSH = 10086
    BLOCKCHAIN_GENESIS_MAINNET = 10101
    CHIADO_TESTNET = 10200
    _0XTADE = 10248
    NUMBERS_MAINNET = 10507
    NUMBERS_TESTNET = 10508
    CRYPTOCOINPAY = 10823
    QUADRANS_BLOCKCHAIN = 10946
    QUADRANS_BLOCKCHAIN_TESTNET = 10947
    ASTRA = 11110
    WAGMI = 11111
    ASTRA_TESTNET = 11115
    HAQQ_NETWORK = 11235
    SHYFT_TESTNET = 11437
    SARDIS_TESTNET = 11612
    SANR_CHAIN = 11888
    SINGULARITY_ZERO_TESTNET = 12051
    SINGULARITY_ZERO_MAINNET = 12052
    STEP_TESTNET = 12345
    SPS = 13000
    CREDIT_SMARTCHAIN_MAINNET = 13308
    PHOENIX_MAINNET = 13381
    SUSONO = 13812
    SPS_TESTNET = 14000
    TRUST_EVM_TESTNET = 15555
    METADOT_MAINNET = 16000
    METADOT_TESTNET = 16001
    IVAR_CHAIN_TESTNET = 16888
    FRONTIER_OF_DREAMS_TESTNET = 18000
    PROOF_OF_MEMES = 18159
    HOME_VERSE_MAINNET = 19011
    BTCIX_NETWORK = 19845
    CALLISTO_TESTNET = 20729
    P12_CHAIN = 20736
    CENNZNET_AZALEA = 21337
    OMCHAIN_MAINNET = 21816
    TAYCAN = 22023
    MAP_MAINNET = 22776
    OPSIDE_TESTNET = 23118
    OASIS_SAPPHIRE = 23294
    OASIS_SAPPHIRE_TESTNET = 23295
    WEBCHAIN = 24484
    MINTME_COM_COIN = 24734
    HAMMER_CHAIN_MAINNET = 25888
    BITKUB_CHAIN_TESTNET = 25925
    HERTZ_NETWORK_MAINNET = 26600
    OASISCHAIN_MAINNET = 26863
    OPTIMISM_BEDROCK_GOERLI_ALPHA_TESTNET = 28528
    PIECE_TESTNET = 30067
    ETHERSOCIAL_NETWORK = 31102
    CLOUDTX_MAINNET = 31223
    CLOUDTX_TESTNET = 31224
    GOCHAIN_TESTNET = 31337
    FILECOIN_WALLABY_TESTNET = 31415
    BITGERT_MAINNET = 32520
    FUSION_MAINNET = 32659
    AVES_MAINNET = 33333
    J2O_TARO = 35011
    Q_MAINNET = 35441
    Q_TESTNET = 35443
    ENERGI_MAINNET = 39797
    OHO_MAINNET = 39815
    OPULENT_X_BETA = 41500
    PEGGLECOIN = 42069
    ARBITRUM_ONE = 42161
    ARBITRUM_NOVA = 42170
    CELO_MAINNET = 42220
    OASIS_EMERALD_TESTNET = 42261
    OASIS_EMERALD = 42262
    ATHEREUM = 43110
    AVALANCHE_FUJI_TESTNET = 43113
    AVALANCHE_C_CHAIN = 43114
    BOBA_AVAX = 43288
    CELO_ALFAJORES_TESTNET = 44787
    AUTOBAHN_NETWORK = 45000
    FUSION_TESTNET = 46688
    REI_NETWORK = 47805
    FLORIPA = 49049
    BIFROST_TESTNET1 = 49088
    ENERGI_TESTNET = 49797
    LIVEPLEX_ORACLEEVM = 50001
    GTON_TESTNET = 50021
    SARDIS_MAINNET = 51712
    DFK_CHAIN = 53935
    HAQQ_CHAIN_TESTNET = 54211
    REI_CHAIN_MAINNET = 55555
    REI_CHAIN_TESTNET = 55556
    BOBA_BNB_MAINNET = 56288
    LINEA_TESTNET = 59140
    THINKIUM_TESTNET_CHAIN_0 = 60000
    THINKIUM_TESTNET_CHAIN_1 = 60001
    THINKIUM_TESTNET_CHAIN_2 = 60002
    THINKIUM_TESTNET_CHAIN_103 = 60103
    ETICA_MAINNET = 61803
    DOKEN_SUPER_CHAIN_MAINNET = 61916
    CELO_BAKLAVA_TESTNET = 62320
    MULTIVAC_MAINNET = 62621
    ECREDITS_MAINNET = 63000
    ECREDITS_TESTNET = 63001
    SIRIUSNET = 67390
    CONDRIEU = 69420
    THINKIUM_MAINNET_CHAIN_0 = 70000
    THINKIUM_MAINNET_CHAIN_1 = 70001
    THINKIUM_MAINNET_CHAIN_2 = 70002
    THINKIUM_MAINNET_CHAIN_103 = 70103
    POLYJUICE_TESTNET = 71393
    GODWOKEN_TESTNET_V1 = 71401
    GODWOKEN_MAINNET = 71402
    ENERGY_WEB_VOLTA_TESTNET = 73799
    MIXIN_VIRTUAL_MACHINE = 73927
    RESINCOIN_MAINNET = 75000
    VENTION_SMART_CHAIN_MAINNET = 77612
    FIRENZE_TEST_NETWORK = 78110
    GOLD_SMART_CHAIN_TESTNET = 79879
    MUMBAI = 80001
    BASE_GOERLI_TESTNET = 84531
    IVAR_CHAIN_MAINNET = 88888
    BEVERLY_HILLS = 90210
    LAMBDA_TESTNET = 92001
    BOBA_BNB_MAINNET_OLD = 97288
    UB_SMART_CHAIN_TESTNET = 99998
    UB_SMART_CHAIN = 99999
    QUARKCHAIN_MAINNET_ROOT = 100000
    QUARKCHAIN_MAINNET_SHARD_0 = 100001
    QUARKCHAIN_MAINNET_SHARD_1 = 100002
    QUARKCHAIN_MAINNET_SHARD_2 = 100003
    QUARKCHAIN_MAINNET_SHARD_3 = 100004
    QUARKCHAIN_MAINNET_SHARD_4 = 100005
    QUARKCHAIN_MAINNET_SHARD_5 = 100006
    QUARKCHAIN_MAINNET_SHARD_6 = 100007
    QUARKCHAIN_MAINNET_SHARD_7 = 100008
    DEPRECATED_CHIADO_TESTNET = 100100
    SOVERUN_TESTNET = 101010
    CRYSTALEUM = 103090
    BROCHAIN_MAINNET = 108801
    QUARKCHAIN_DEVNET_ROOT = 110000
    QUARKCHAIN_DEVNET_SHARD_0 = 110001
    QUARKCHAIN_DEVNET_SHARD_1 = 110002
    QUARKCHAIN_DEVNET_SHARD_2 = 110003
    QUARKCHAIN_DEVNET_SHARD_3 = 110004
    QUARKCHAIN_DEVNET_SHARD_4 = 110005
    QUARKCHAIN_DEVNET_SHARD_5 = 110006
    QUARKCHAIN_DEVNET_SHARD_6 = 110007
    QUARKCHAIN_DEVNET_SHARD_7 = 110008
    ETND_CHAIN_MAINNETS = 131419
    CONDOR_TEST_NETWORK = 188881
    MILKOMEDA_C1_TESTNET = 200101
    MILKOMEDA_A1_TESTNET = 200202
    AKROMA = 200625
    ALAYA_MAINNET = 201018
    ALAYA_DEV_TESTNET = 201030
    MYTHICAL_CHAIN = 201804
    DECIMAL_SMART_CHAIN_TESTNET = 202020
    JELLIE = 202624
    PLATON_MAINNET = 210425
    MAS_MAINNET = 220315
    HAYMO_TESTNET = 234666
    ARTIS_SIGMA1 = 246529
    ARTIS_TESTNET_TAU1 = 246785
    CMP_MAINNET = 256256
    GEAR_ZERO_NETWORK_TESTNET = 266256
    SOCIAL_SMART_CHAIN_MAINNET = 281121
    FILECOIN_CALIBRATION_TESTNET = 314159
    POLIS_TESTNET = 333888
    POLIS_MAINNET = 333999
    METAL_C_CHAIN = 381931
    METAL_TAHOE_C_CHAIN = 381932
    KEKCHAIN = 420420
    KEKCHAIN_KEKTEST = 420666
    ARBITRUM_RINKEBY = 421611
    ARBITRUM_GOERLI = 421613
    DEXALOT_SUBNET_TESTNET = 432201
    DEXALOT_SUBNET = 432204
    WEELINK_TESTNET = 444900
    OPENCHAIN_MAINNET = 474142
    CMP_TESTNET = 512512
    ETHEREUM_FAIR = 513100
    SCROLL = 534352
    SCROLL_GOERLI_TESTNET = 534353
    SCROLL_PRE_ALPHA_TESTNET = 534354
    BEAR_NETWORK_CHAIN_MAINNET = 641230
    VISION_VPIONEER_TEST_CHAIN = 666666
    OCTASPACE = 800001
    _4GOODNETWORK = 846000
    VISION_MAINNET = 888888
    POSICHAIN_MAINNET_SHARD_0 = 900000
    POSICHAIN_TESTNET_SHARD_0 = 910000
    POSICHAIN_DEVNET_SHARD_0 = 920000
    POSICHAIN_DEVNET_SHARD_1 = 920001
    FNCY_TESTNET = 923018
    ELUVIO_CONTENT_FABRIC = 955305
    ETHO_PROTOCOL = 1313114
    XEROM = 1313500
    KINTSUGI = 1337702
    KILN = 1337802
    ZHEJIANG = 1337803
    PLIAN_MAINNET_MAIN = 2099156
    PLATON_DEV_TESTNET_DEPRECATED = 2203181
    PLATON_DEV_TESTNET2 = 2206132
    FILECOIN_BUTTERFLY_TESTNET = 3141592
    IMVERSED_MAINNET = 5555555
    IMVERSED_TESTNET = 5555558
    OPENVESSEL = 7355310
    QL1_TESTNET = 7668378
    MUSICOIN = 7762959
    PLIAN_MAINNET_SUBCHAIN_1 = 8007736
    PLIAN_TESTNET_SUBCHAIN_1 = 10067275
    SOVERUN_MAINNET = 10101010
    SEPOLIA = 11155111
    PEPCHAIN_CHURCHILL = 13371337
    ANDUSCHAIN_MAINNET = 14288640
    PLIAN_TESTNET_MAIN = 16658437
    IOLITE = 18289463
    SMARTMESH_MAINNET = 20180430
    QUARKBLOCKCHAIN = 20181205
    EXCELON_MAINNET = 22052002
    EXCOINCIAL_CHAIN_VOLTA_TESTNET = 27082017
    EXCOINCIAL_CHAIN_MAINNET = 27082022
    AUXILIUM_NETWORK_MAINNET = 28945486
    FLACHAIN_MAINNET = 29032022
    FILECOIN_LOCAL_TESTNET = 31415926
    JOYS_DIGITAL_MAINNET = 35855456
    MAISTESTSUBNET = 43214913
    AQUACHAIN = 61717561
    JOYS_DIGITAL_TESTNET = 99415706
    GATHER_MAINNET_NETWORK = 192837465
    NEON_EVM_DEVNET = 245022926
    NEON_EVM_MAINNET = 245022934
    NEON_EVM_TESTNET = 245022940
    ONELEDGER_MAINNET = 311752642
    CALYPSO_NFT_HUB_SKALE_TESTNET = 344106930
    GATHER_TESTNET_NETWORK = 356256156
    GATHER_DEVNET_NETWORK = 486217935
    NEBULA_STAGING = 503129905
    IPOS_NETWORK = 1122334455
    AURORA_MAINNET = 1313161554
    AURORA_TESTNET = 1313161555
    AURORA_BETANET = 1313161556
    NEBULA_MAINNET = 1482601649
    CALYPSO_NFT_HUB_SKALE = 1564830818
    HARMONY_MAINNET_SHARD_0 = 1666600000
    HARMONY_MAINNET_SHARD_1 = 1666600001
    HARMONY_MAINNET_SHARD_2 = 1666600002
    HARMONY_MAINNET_SHARD_3 = 1666600003
    HARMONY_TESTNET_SHARD_0 = 1666700000
    HARMONY_TESTNET_SHARD_1 = 1666700001
    HARMONY_TESTNET_SHARD_2 = 1666700002
    HARMONY_TESTNET_SHARD_3 = 1666700003
    HARMONY_DEVNET_SHARD_0 = 1666900000
    DATAHOPPER = 2021121117
    EUROPA_SKALE_CHAIN = 2046399126
    PIRL = 3125659152
    ONELEDGER_TESTNET_FRANKENSTEIN = 4216137055
    PALM_TESTNET = 11297108099
    PALM = 11297108109
    NTITY_MAINNET = 197710212030
    HARADEV_TESTNET = 197710212031
    ZENIQ = 383414847825
    PDC_MAINNET = 666301171999
    MOLEREUM_NETWORK = 6022140761023

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN
