

```python
import networkx as nx
import seaborn
import skbio as sb
import matplotlib.pyplot as plt
import csv
%matplotlib inline
```


```python
G = nx.read_weighted_edgelist('/Users/jasonblues/Desktop/Project_files/edges.txt',create_using=nx.MultiGraph())
G.nodes()
G.edges(data=True)
```




    [('3L0A3_003', 'GL890970', {'weight': 23573.0}),
     ('GL890970', '3L0A3_004', {'weight': 27976.0}),
     ('GL890970', '3L0A3_004', {'weight': 9649.0}),
     ('GL890970', 'JHB0A2_004', {'weight': 14295.0}),
     ('GL890970', 'PAL0A1_003', {'weight': 15458.0}),
     ('GL890970', 'PAL0A1_004', {'weight': 5363.0}),
     ('GL890970', 'PAL0A1_004', {'weight': 6607.0}),
     ('GL890970', 'PAL0A1_005', {'weight': 5234.0}),
     ('3L0A3_004', 'PNG0A4_003', {'weight': 18086.0}),
     ('3L0A3_004', 'PAL0A1_016', {'weight': 12123.0}),
     ('3L0A3_006', 'GL890941', {'weight': 8206.0}),
     ('GL890941', 'JHB0A2_008', {'weight': 7591.0}),
     ('3L0A3_007', 'GL890825', {'weight': 19014.0}),
     ('3L0A3_007', 'PAL0A1_007', {'weight': 8514.0}),
     ('GL890825', '3L0A3_031', {'weight': 9674.0}),
     ('GL890825', 'JHB0A2_009', {'weight': 5785.0}),
     ('3L0A3_008', 'GL890820', {'weight': 6485.0}),
     ('3L0A3_008', 'JHB0A2_011', {'weight': 16368.0}),
     ('GL890820', 'ASI1E3_001', {'weight': 6840.0}),
     ('3L0A3_010', 'GL890823', {'weight': 6848.0}),
     ('3L0A3_010', 'PAL0A1_012', {'weight': 12675.0}),
     ('3L0A3_010', 'JHB0A2_016', {'weight': 5620.0}),
     ('3L0A3_010', 'ASI1E3_006', {'weight': 7518.0}),
     ('3L0A3_010', 'PAL1D4_019', {'weight': 5619.0}),
     ('GL890823', '3L0A3_011', {'weight': 32073.0}),
     ('3L0A3_013', 'BGC0001001', {'weight': 5202.0}),
     ('BGC0001001', 'ASI1E3_021', {'weight': 8496.0}),
     ('BGC0001001', 'ASI1E3_028', {'weight': 10849.0}),
     ('BGC0001001', 'JHB0A2_023', {'weight': 12143.0}),
     ('BGC0001001', 'JHB0A2_036', {'weight': 15639.0}),
     ('BGC0001001', 'JHB0A2_036', {'weight': 20785.0}),
     ('BGC0001001', 'PAL0A1_035', {'weight': 31147.0}),
     ('BGC0001001', 'PAL1D4_023', {'weight': 10307.0}),
     ('BGC0001001', 'PNG3F7_024', {'weight': 8739.0}),
     ('3L0A3_015', 'GL890930', {'weight': 9893.0}),
     ('3L0A3_015', 'PNG3F7_006', {'weight': 6696.0}),
     ('GL890930', 'ASI1E3_032', {'weight': 9646.0}),
     ('GL890930', 'JHB0A2_026', {'weight': 8153.0}),
     ('GL890930', 'PAL0A1_024', {'weight': 7266.0}),
     ('GL890930', 'PNG0A4_020', {'weight': 7217.0}),
     ('3L0A3_017', 'CP003284', {'weight': 7239.0}),
     ('3L0A3_017', 'BGC0000302', {'weight': 7239.0}),
     ('3L0A3_021', 'GL890969', {'weight': 23545.0}),
     ('GL890969', 'JHB0A2_035', {'weight': 6786.0}),
     ('3L0A3_024', 'GL890827', {'weight': 12975.0}),
     ('3L0A3_024', 'PAL0A1_038', {'weight': 6507.0}),
     ('GL890827', 'JHB0A2_039', {'weight': 11875.0}),
     ('3L0A3_030', 'GL890840', {'weight': 7169.0}),
     ('3L0A3_030', 'GL890840', {'weight': 13804.0}),
     ('GL890840', 'ASI1E3_012', {'weight': 23025.0}),
     ('GL890840', 'JHB0A2_007', {'weight': 25350.0}),
     ('GL890840', 'PAL0A1_043', {'weight': 6841.0}),
     ('GL890840', 'PAL0A1_043', {'weight': 7034.0}),
     ('GL890840', 'PAL1D4_014', {'weight': 12357.0}),
     ('ASI1E3_001', 'JHB0A2_011', {'weight': 14426.0}),
     ('ASI1E3_002', 'CM002803', {'weight': 6651.0}),
     ('ASI1E3_002', 'PAL0A1_019', {'weight': 47192.0}),
     ('CM002803', 'JHB0A2_022', {'weight': 6758.0}),
     ('CM002803', 'PAL1D4_021', {'weight': 5610.0}),
     ('ASI1E3_018', 'CP001037', {'weight': 6134.0}),
     ('ASI1E3_018', 'PNG0A4_005', {'weight': 27426.0}),
     ('CP001037', 'ASI1E3_028', {'weight': 7156.0}),
     ('CP001037', 'ASX1E4_019', {'weight': 9209.0}),
     ('ASI1E3_021', 'GL890975', {'weight': 7187.0}),
     ('ASI1E3_021', 'GL890975', {'weight': 11792.0}),
     ('ASI1E3_021', 'BGC0000976', {'weight': 13061.0}),
     ('ASI1E3_021', 'AY652953', {'weight': 13059.0}),
     ('ASI1E3_021', 'CP000393', {'weight': 5295.0}),
     ('GL890975', 'ASI1E3_028', {'weight': 15001.0}),
     ('GL890975', 'JHB0A2_023', {'weight': 17530.0}),
     ('GL890975', 'JHB0A2_036', {'weight': 23999.0}),
     ('GL890975', 'PAL0A1_035', {'weight': 66760.0}),
     ('GL890975', 'PAL1D4_023', {'weight': 22687.0}),
     ('GL890975', 'PNG3F7_024', {'weight': 10499.0}),
     ('BGC0000976', 'ASI1E3_028', {'weight': 15001.0}),
     ('BGC0000976', 'JHB0A2_023', {'weight': 19344.0}),
     ('BGC0000976', 'JHB0A2_036', {'weight': 25949.0}),
     ('BGC0000976', 'PAL0A1_035', {'weight': 73116.0}),
     ('BGC0000976', 'PAL1D4_023', {'weight': 24616.0}),
     ('BGC0000976', 'PNG3F7_024', {'weight': 12822.0}),
     ('AY652953', 'ASI1E3_028', {'weight': 15001.0}),
     ('AY652953', 'JHB0A2_023', {'weight': 6782.0}),
     ('AY652953', 'JHB0A2_023', {'weight': 20068.0}),
     ('AY652953', 'JHB0A2_036', {'weight': 25943.0}),
     ('AY652953', 'PAL0A1_035', {'weight': 73989.0}),
     ('AY652953', 'PAL1D4_023', {'weight': 24612.0}),
     ('AY652953', 'PNG3F7_024', {'weight': 12816.0}),
     ('ASI1E3_028', 'PNG3F7_011', {'weight': 10692.0}),
     ('ASI1E3_028', 'ISBH3F3_004', {'weight': 5503.0}),
     ('ASI1E3_028', 'PNG3F7_032', {'weight': 5063.0}),
     ('ASI1E3_028', 'PNG0A4_016', {'weight': 11384.0}),
     ('ASI1E3_032', 'PNG3F7_006', {'weight': 6709.0}),
     ('ASX1E4_001', 'HG966617', {'weight': 5050.0}),
     ('HG966617', 'ASX1E4_017', {'weight': 11157.0}),
     ('HG966617', 'ASX1E4_018', {'weight': 8215.0}),
     ('ASX1E4_019', 'CP003597', {'weight': 7217.0}),
     ('ASX1E4_019', 'CP003630', {'weight': 5284.0}),
     ('CP003630', 'CHN1D9_011', {'weight': 8506.0}),
     ('ASX1E4_025', 'JTCM01000002', {'weight': 11372.0}),
     ('JHB0A2_004', 'PNG3F7_005', {'weight': 10283.0}),
     ('JHB0A2_009', 'PAL0A1_007', {'weight': 18856.0}),
     ('JHB0A2_022', 'PAL0A1_019', {'weight': 24377.0}),
     ('JHB0A2_023', 'PNG0A4_016', {'weight': 19689.0}),
     ('JHB0A2_023', 'PNG0A4_005', {'weight': 12015.0}),
     ('JHB0A2_023', 'PNG3F7_011', {'weight': 13092.0}),
     ('JHB0A2_026', 'PNG3F7_006', {'weight': 6723.0}),
     ('JHB0A2_034', 'CP003642', {'weight': 5359.0}),
     ('JHB0A2_034', 'PAL0A1_033', {'weight': 24888.0}),
     ('CP003642', 'PAL0A1_037', {'weight': 11027.0}),
     ('CP003642', 'PAL1D4_037', {'weight': 7460.0}),
     ('JHB0A2_039', 'PAL0A1_038', {'weight': 9837.0}),
     ('PAL0A1_003', 'PNG3F7_016', {'weight': 22883.0}),
     ('PAL0A1_003', 'PNG3F7_016', {'weight': 7972.0}),
     ('PAL0A1_003', 'PNG0A4_002', {'weight': 6945.0}),
     ('PAL0A1_003', 'PNG0A4_002', {'weight': 8500.0}),
     ('PAL0A1_008', 'CP002059', {'weight': 5557.0}),
     ('CP002059', 'PAL1D4_004', {'weight': 4985.0}),
     ('CP002059', 'PNG0A4_006', {'weight': 5542.0}),
     ('PAL0A1_009', 'BGC0001000', {'weight': 9223.0}),
     ('PAL0A1_009', 'PAL0A1_033', {'weight': 7019.0}),
     ('BGC0001000', 'PNG0A4_007', {'weight': 9851.0}),
     ('BGC0001000', 'PNG3F7_002', {'weight': 9287.0}),
     ('PAL0A1_028', 'CP003590', {'weight': 9449.0}),
     ('PAL0A1_028', 'PNG3F7_011', {'weight': 14248.0}),
     ('PAL0A1_028', 'ISBH3F3_004', {'weight': 12024.0}),
     ('PAL0A1_028', 'ASI1E3_023', {'weight': 6011.0}),
     ('PAL0A1_028', 'ASI1E3_023', {'weight': 5819.0}),
     ('PAL0A1_037', 'BGC0000017', {'weight': 10690.0}),
     ('PAL0A1_037', 'CACA01000369', {'weight': 5308.0}),
     ('PAL0A1_037', 'KM245024', {'weight': 5187.0}),
     ('PAL0A1_037', 'KM245023', {'weight': 5186.0}),
     ('BGC0000017', 'PAL1D4_037', {'weight': 7292.0}),
     ('PAL1D4_005', 'AAUW01000004', {'weight': 7217.0}),
     ('PAL1D4_005', 'AXCE01000034', {'weight': 7287.0}),
     ('PAL1D4_005', 'AXBY01000005', {'weight': 7287.0}),
     ('PAL1D4_005', 'CP002568', {'weight': 5420.0}),
     ('PAL1D4_005', 'GL476320', {'weight': 5662.0}),
     ('PAL1D4_008', 'BGC0001161', {'weight': 5883.0}),
     ('PAL1D4_008', 'BGC0001163', {'weight': 5716.0}),
     ('PAL1D4_008', 'BGC0001162', {'weight': 5707.0}),
     ('PAL1D4_008', 'PAL0A1_007', {'weight': 17409.0}),
     ('BGC0001161', 'PNG0A4_019', {'weight': 6279.0}),
     ('BGC0001163', 'PNG0A4_019', {'weight': 5688.0}),
     ('BGC0001162', 'PNG0A4_019', {'weight': 5649.0}),
     ('PAL1D4_018', 'BGC0000043', {'weight': 6335.0}),
     ('PAL1D4_021', 'PAL0A1_019', {'weight': 17171.0}),
     ('PAL1D4_023', 'PNG3F7_011', {'weight': 16735.0}),
     ('PAL1D4_023', 'PNG0A4_005', {'weight': 11289.0}),
     ('PAL1D4_023', 'PNG3F7_010', {'weight': 6998.0}),
     ('PAL1D4_023', 'PNG0A4_016', {'weight': 9244.0}),
     ('PAL1D4_023', 'ISBH3F3_004', {'weight': 7234.0}),
     ('PAL1D4_027', 'AY974560', {'weight': 6800.0}),
     ('PAP1D6_008', 'AANB01000007', {'weight': 6489.0}),
     ('PAP1D6_008', 'JAMD01000001', {'weight': 6154.0}),
     ('PAP1D6_008', 'GG703520', {'weight': 6475.0}),
     ('PAP1D6_008', 'JWLF01000002', {'weight': 6383.0}),
     ('PAP1D6_008', 'JWLH01000003', {'weight': 6380.0}),
     ('PAP1D6_008', 'JWLE01000001', {'weight': 6374.0}),
     ('PNG0A4_019', 'PAL0A1_007', {'weight': 5857.0}),
     ('PNG0A4_020', 'PNG3F7_006', {'weight': 8669.0}),
     ('PNG3F7_024', 'PNG0A4_016', {'weight': 20416.0}),
     ('PNG3F7_024', 'PNG0A4_016', {'weight': 5139.0}),
     ('3L0A3_002', 'JHB0A2_001', {'weight': 18938.0}),
     ('JHB0A2_001', 'JHB0A2_001', {'weight': 30814.0}),
     ('PNG0A4_003', 'JHB0A2_019', {'weight': 5175.0}),
     ('PNG0A4_003', 'PNG0A4_003', {'weight': 43537.0}),
     ('PAL0A1_016', 'ASI1E3_007', {'weight': 17479.0}),
     ('PAL0A1_016', 'JHB0A2_017', {'weight': 11520.0}),
     ('PAL0A1_016', 'JHB0A2_017', {'weight': 25776.0}),
     ('PAL0A1_016', 'JHB0A2_019', {'weight': 7978.0}),
     ('PAL0A1_016', 'PAL0A1_014', {'weight': 23514.0}),
     ('PAL0A1_016', 'PAL0A1_016', {'weight': 54795.0}),
     ('PAL0A1_016', 'PAL1D4_024', {'weight': 15889.0}),
     ('PAL0A1_016', 'PAL1D4_033', {'weight': 5579.0}),
     ('PAL0A1_016', 'PAL1D4_033', {'weight': 6401.0}),
     ('PAL0A1_016', 'PNG3F7_003', {'weight': 6308.0}),
     ('PAL0A1_007', 'ASI1E3_020', {'weight': 9377.0}),
     ('PAL0A1_007', 'PAL0A1_007', {'weight': 22325.0}),
     ('PAL0A1_007', 'PNG3F7_014', {'weight': 18508.0}),
     ('JHB0A2_011', 'JHB0A2_011', {'weight': 22095.0}),
     ('PAL0A1_012', 'PAL0A1_012', {'weight': 41951.0}),
     ('PAL0A1_012', 'PAL1D4_019', {'weight': 6321.0}),
     ('PAL0A1_012', 'PNG0A4_012', {'weight': 12752.0}),
     ('JHB0A2_016', 'ASI1E3_006', {'weight': 5043.0}),
     ('ASI1E3_006', 'ASI1E3_006', {'weight': 5279.0}),
     ('PNG3F7_006', 'PAL1D4_017', {'weight': 7267.0}),
     ('PNG3F7_006', 'PAL1D4_017', {'weight': 7267.0}),
     ('PNG3F7_006', 'PNG3F7_006', {'weight': 11154.0}),
     ('3L0A3_016', '3L0A3_016', {'weight': 12848.0}),
     ('3L0A3_016', 'PNG3F7_020', {'weight': 9799.0}),
     ('3L0A3_016', 'PNG3F7_020', {'weight': 9736.0}),
     ('3L0A3_016', 'PAL0A1_025', {'weight': 8847.0}),
     ('3L0A3_016', 'JHB0A2_029', {'weight': 8733.0}),
     ('3L0A3_016', 'ASI1E3_033', {'weight': 7507.0}),
     ('3L0A3_016', 'PNG0A4_021', {'weight': 8140.0}),
     ('PNG3F7_020', 'PAL0A1_025', {'weight': 6498.0}),
     ('PNG3F7_020', 'PAL0A1_025', {'weight': 10092.0}),
     ('PNG3F7_020', 'PNG0A4_021', {'weight': 8664.0}),
     ('PNG3F7_020', 'PNG0A4_021', {'weight': 8917.0}),
     ('PNG3F7_020', 'PNG3F7_020', {'weight': 12072.0}),
     ('PNG3F7_020', 'ASI1E3_033', {'weight': 7529.0}),
     ('PNG3F7_020', 'JHB0A2_029', {'weight': 8600.0}),
     ('PAL0A1_025', 'PAL0A1_025', {'weight': 6046.0}),
     ('PAL0A1_025', 'PNG0A4_021', {'weight': 7650.0}),
     ('JHB0A2_029', 'JHB0A2_029', {'weight': 6141.0}),
     ('3L0A3_018', '3L0A3_018', {'weight': 8614.0}),
     ('3L0A3_018', 'PNG0A4_022', {'weight': 8278.0}),
     ('3L0A3_018', 'PNG0A4_022', {'weight': 8278.0}),
     ('3L0A3_018', 'PAL0A1_027', {'weight': 8268.0}),
     ('3L0A3_018', 'PAL0A1_027', {'weight': 8268.0}),
     ('3L0A3_018', 'PAL1D4_003', {'weight': 8149.0}),
     ('3L0A3_018', 'JHB0A2_028', {'weight': 7389.0}),
     ('3L0A3_018', 'JHB0A2_028', {'weight': 7389.0}),
     ('PNG0A4_022', 'JHB0A2_028', {'weight': 7346.0}),
     ('PNG0A4_022', 'JHB0A2_028', {'weight': 7346.0}),
     ('PNG0A4_022', 'PAL0A1_027', {'weight': 8389.0}),
     ('PNG0A4_022', 'PAL0A1_027', {'weight': 8389.0}),
     ('PNG0A4_022', 'PNG0A4_022', {'weight': 8603.0}),
     ('PNG0A4_022', 'PAL1D4_003', {'weight': 8269.0}),
     ('PAL0A1_027', 'JHB0A2_028', {'weight': 7302.0}),
     ('PAL0A1_027', 'JHB0A2_028', {'weight': 7302.0}),
     ('PAL0A1_027', 'PAL0A1_027', {'weight': 8746.0}),
     ('PAL0A1_027', 'PAL1D4_003', {'weight': 8479.0}),
     ('PAL1D4_003', 'JHB0A2_028', {'weight': 7192.0}),
     ('JHB0A2_028', 'JHB0A2_028', {'weight': 8621.0}),
     ('3L0A3_019', '3L0A3_019', {'weight': 8828.0}),
     ('3L0A3_019', 'PAL0A1_031', {'weight': 10453.0}),
     ('3L0A3_019', 'PAL0A1_031', {'weight': 8276.0}),
     ('3L0A3_019', 'PAL1D4_026', {'weight': 7717.0}),
     ('3L0A3_019', 'PAL1D4_026', {'weight': 6130.0}),
     ('3L0A3_019', 'JHB0A2_032', {'weight': 7034.0}),
     ('3L0A3_019', 'PNG0A4_025', {'weight': 10912.0}),
     ('PAL0A1_031', 'JHB0A2_032', {'weight': 8853.0}),
     ('PAL0A1_031', 'PAL1D4_026', {'weight': 8868.0}),
     ('PAL0A1_031', 'PAL1D4_026', {'weight': 7409.0}),
     ('PAL0A1_031', 'PAL1D4_026', {'weight': 8677.0}),
     ('PAL0A1_031', 'PAL0A1_031', {'weight': 10875.0}),
     ('PAL0A1_031', 'PNG0A4_025', {'weight': 8121.0}),
     ('PAL1D4_026', 'JHB0A2_032', {'weight': 6170.0}),
     ('PAL1D4_026', 'JHB0A2_032', {'weight': 5039.0}),
     ('PAL1D4_026', 'PAL1D4_026', {'weight': 6101.0}),
     ('PAL1D4_026', 'PAL1D4_026', {'weight': 7562.0}),
     ('PAL1D4_026', 'PNG0A4_025', {'weight': 6171.0}),
     ('3L0A3_020', '3L0A3_020', {'weight': 10675.0}),
     ('3L0A3_020', 'PAL1D4_010', {'weight': 5598.0}),
     ('3L0A3_020', 'PAL1D4_010', {'weight': 5598.0}),
     ('3L0A3_020', 'PAL0A1_032', {'weight': 5597.0}),
     ('PAL1D4_010', 'CHN1D9_012', {'weight': 7188.0}),
     ('PAL1D4_010', 'PAL1D4_010', {'weight': 7149.0}),
     ('PAL1D4_010', 'PAL0A1_032', {'weight': 7094.0}),
     ('3L0A3_023', '3L0A3_023', {'weight': 24886.0}),
     ('3L0A3_023', 'PAL0A1_036', {'weight': 15631.0}),
     ('3L0A3_023', 'PAL0A1_036', {'weight': 15683.0}),
     ('3L0A3_023', 'ASI1E3_017', {'weight': 14643.0}),
     ('3L0A3_023', 'ASI1E3_017', {'weight': 14767.0}),
     ('PAL0A1_036', 'ASI1E3_017', {'weight': 20618.0}),
     ('PAL0A1_036', 'ASI1E3_017', {'weight': 20548.0}),
     ('PAL0A1_036', 'PAL0A1_036', {'weight': 26655.0}),
     ('PAL0A1_036', 'PAL1D4_020', {'weight': 16436.0}),
     ('PAL0A1_036', 'PAL1D4_020', {'weight': 5168.0}),
     ('ASI1E3_017', 'ASI1E3_017', {'weight': 28838.0}),
     ('PAL0A1_038', 'PAL0A1_038', {'weight': 12085.0}),
     ('3L0A3_025', 'PAL0A1_034', {'weight': 10705.0}),
     ('PAL0A1_034', 'PAL0A1_034', {'weight': 5920.0}),
     ('PAL0A1_034', 'PAL0A1_034', {'weight': 18073.0}),
     ('PAL0A1_034', 'PAL1D4_009', {'weight': 8551.0}),
     ('PAL0A1_034', 'PAL1D4_009', {'weight': 15153.0}),
     ('3L0A3_026', '3L0A3_026', {'weight': 26943.0}),
     ('3L0A3_026', 'ASI1E3_019', {'weight': 5112.0}),
     ('3L0A3_026', 'PNG3F7_005', {'weight': 5065.0}),
     ('3L0A3_026', 'PNG3F7_005', {'weight': 5635.0}),
     ('3L0A3_027', '3L0A3_027', {'weight': 7169.0}),
     ('PAL0A1_019', 'PAL0A1_019', {'weight': 57770.0}),
     ('PAL0A1_019', 'PAL0A1_022', {'weight': 5347.0}),
     ('PAL0A1_019', 'PNG3F7_013', {'weight': 5312.0}),
     ('ASI1E3_007', 'PAP1D6_003', {'weight': 23328.0}),
     ('ASI1E3_007', 'PAL0A1_014', {'weight': 19952.0}),
     ('PAP1D6_003', 'JHB0A2_017', {'weight': 10726.0}),
     ('PAP1D6_003', 'PAL0A1_014', {'weight': 20499.0}),
     ('PAP1D6_003', 'PAP1D6_003', {'weight': 12249.0}),
     ('PAL0A1_014', 'JHB0A2_017', {'weight': 14413.0}),
     ('PAL0A1_014', 'PAL0A1_014', {'weight': 34872.0}),
     ('PAL0A1_014', 'PAL1D4_033', {'weight': 5575.0}),
     ('PAL0A1_014', 'PAL1D4_033', {'weight': 7380.0}),
     ('ASI1E3_008', 'PAL0A1_010', {'weight': 10763.0}),
     ('ASI1E3_008', 'PAL0A1_010', {'weight': 12638.0}),
     ('ASI1E3_008', 'ISBH3F3_001', {'weight': 6500.0}),
     ('ASI1E3_008', 'ISBH3F3_001', {'weight': 6866.0}),
     ('ASI1E3_008', 'PNG0A4_009', {'weight': 11520.0}),
     ('ASI1E3_008', 'JHB0A2_014', {'weight': 11669.0}),
     ('PAL0A1_010', 'JHB0A2_014', {'weight': 21974.0}),
     ('PAL0A1_010', 'JHB0A2_014', {'weight': 21977.0}),
     ('PAL0A1_010', 'PAL0A1_010', {'weight': 29368.0}),
     ('PAL0A1_010', 'PNG0A4_009', {'weight': 20716.0}),
     ('PAL0A1_010', 'PNG0A4_009', {'weight': 20837.0}),
     ('ISBH3F3_001', 'ISBH3F3_001', {'weight': 22639.0}),
     ('PNG0A4_009', 'PNG0A4_009', {'weight': 27866.0}),
     ('JHB0A2_014', 'JHB0A2_014', {'weight': 29256.0}),
     ('ASI1E3_009', 'ASI1E3_009', {'weight': 14710.0}),
     ('ASI1E3_010', 'PNG3F7_004', {'weight': 5224.0}),
     ('PNG3F7_004', 'PNG3F7_004', {'weight': 11783.0}),
     ('ASI1E3_013', 'ASI1E3_013', {'weight': 23490.0}),
     ('ASI1E3_013', 'JHB0A2_020', {'weight': 14180.0}),
     ('ASI1E3_013', 'JHB0A2_020', {'weight': 14134.0}),
     ('ASI1E3_013', 'PAL0A1_018', {'weight': 11475.0}),
     ('JHB0A2_020', 'JHB0A2_020', {'weight': 24359.0}),
     ('PAL0A1_018', 'PAL0A1_018', {'weight': 22100.0}),
     ('PAL0A1_018', 'PAL1D4_022', {'weight': 12239.0}),
     ('ASI1E3_014', 'ASI1E3_014', {'weight': 19608.0}),
     ('ASI1E3_016', 'ASI1E3_016', {'weight': 7403.0}),
     ('PNG0A4_005', 'JHB0A2_006', {'weight': 14396.0}),
     ('PNG0A4_005', 'PNG0A4_005', {'weight': 9925.0}),
     ('ASI1E3_019', 'NAK4C8_005', {'weight': 7629.0}),
     ('ASI1E3_019', 'NAK4C8_005', {'weight': 5017.0}),
     ('ASI1E3_019', 'NAK4C8_005', {'weight': 14151.0}),
     ('NAK4C8_005', 'CHN1D9_003', {'weight': 15262.0}),
     ('NAK4C8_005', 'NAK4C8_005', {'weight': 28182.0}),
     ('ASI1E3_022', 'ASI1E3_022', {'weight': 23146.0}),
     ('ASI1E3_023', 'ASI1E3_023', {'weight': 22546.0}),
     ('ASI1E3_024', 'ASI1E3_024', {'weight': 7864.0}),
     ('PNG3F7_011', 'CHN1D9_004', {'weight': 9965.0}),
     ('PNG3F7_011', 'PNG3F7_011', {'weight': 30886.0}),
     ('ISBH3F3_004', 'ISBH3F3_004', {'weight': 60537.0}),
     ('PNG0A4_016', 'PNG0A4_016', {'weight': 48988.0}),
     ('ASI1E3_030', 'JHB0A2_024', {'weight': 6269.0}),
     ('ASI1E3_030', 'PAL0A1_022', {'weight': 4998.0}),
     ('JHB0A2_024', 'JHB0A2_024', {'weight': 9349.0}),
     ('JHB0A2_024', 'PAL0A1_022', {'weight': 4998.0}),
     ('PAL0A1_022', 'PAL0A1_022', {'weight': 10290.0}),
     ('PAL0A1_022', 'PNG3F7_013', {'weight': 5582.0}),
     ('PAL0A1_022', 'PNG3F7_013', {'weight': 5562.0}),
     ('ASI1E3_031', 'ASI1E3_031', {'weight': 9715.0}),
     ('ASI1E3_034', 'ASI1E3_034', {'weight': 20492.0}),
     ('ASX1E4_002', 'ASX1E4_002', {'weight': 11586.0}),
     ('ASX1E4_003', 'PNG3F7_003', {'weight': 5651.0}),
     ('PNG3F7_003', 'NAK4C8_004', {'weight': 13460.0}),
     ('PNG3F7_003', 'PAL1D4_015', {'weight': 10426.0}),
     ('PNG3F7_003', 'PNG3F7_003', {'weight': 6821.0}),
     ('PNG3F7_003', 'PNG0A4_013', {'weight': 6604.0}),
     ('ASX1E4_004', 'ASX1E4_004', {'weight': 22559.0}),
     ('ASX1E4_005', 'ASX1E4_005', {'weight': 9619.0}),
     ('ASX1E4_007', 'ASX1E4_007', {'weight': 11896.0}),
     ('ASX1E4_008', 'ASX1E4_008', {'weight': 32525.0}),
     ('ASX1E4_009', 'ASX1E4_009', {'weight': 12366.0}),
     ('ASX1E4_010', 'ASX1E4_010', {'weight': 26479.0}),
     ('ASX1E4_011', 'ASX1E4_011', {'weight': 13526.0}),
     ('ASX1E4_013', 'CHN1D9_001', {'weight': 13092.0}),
     ('CHN1D9_001', 'CHN1D9_001', {'weight': 24332.0}),
     ('ASX1E4_014', 'ASX1E4_014', {'weight': 27411.0}),
     ('ASX1E4_015', 'ASX1E4_015', {'weight': 12760.0}),
     ('ASX1E4_016', 'ASX1E4_016', {'weight': 5936.0}),
     ('ASX1E4_020', 'ASX1E4_020', {'weight': 13516.0}),
     ('ASX1E4_021', 'ASX1E4_021', {'weight': 5232.0}),
     ('ASX1E4_022', 'ASX1E4_022', {'weight': 11698.0}),
     ('ASX1E4_023', 'ASX1E4_023', {'weight': 12189.0}),
     ('ASX1E4_024', 'STM4C5_004', {'weight': 18374.0}),
     ('STM4C5_004', 'PAB3F5_003', {'weight': 11665.0}),
     ('STM4C5_004', 'STM4C5_004', {'weight': 16758.0}),
     ('ASX1E4_026', 'ASX1E4_026', {'weight': 17707.0}),
     ('ASX1E4_027', 'ASX1E4_027', {'weight': 11459.0}),
     ('ASX1E4_028', 'ASX1E4_028', {'weight': 8505.0}),
     ('ASX1E4_029', 'ASX1E4_029', {'weight': 8903.0}),
     ('ASX1E4_030', 'ASX1E4_030', {'weight': 6061.0}),
     ('CHN1D9_002', 'ISBH3F3_003', {'weight': 28248.0}),
     ('ISBH3F3_003', 'ISBH3F3_003', {'weight': 18670.0}),
     ('CHN1D9_005', 'CHN1D9_005', {'weight': 17920.0}),
     ('CHN1D9_009', 'CHN1D9_009', {'weight': 17307.0}),
     ('CHN1D9_010', 'CHN1D9_010', {'weight': 7770.0}),
     ('CHN1D9_013', 'CHN1D9_013', {'weight': 10319.0}),
     ('CHN1D9_014', 'CHN1D9_014', {'weight': 12649.0}),
     ('CHN1D9_015', 'CHN1D9_015', {'weight': 11575.0}),
     ('CHN1D9_016', 'CHN1D9_016', {'weight': 10869.0}),
     ('ISBH3F3_002', 'STM4C5_003', {'weight': 5350.0}),
     ('STM4C5_003', 'NAK4C8_002', {'weight': 13596.0}),
     ('STM4C5_003', 'NAK4C8_002', {'weight': 13197.0}),
     ('STM4C5_003', 'STM4C5_003', {'weight': 21128.0}),
     ('ISBH3F3_005', 'ISBH3F3_005', {'weight': 18833.0}),
     ('ISBH3F3_006', 'ISBH3F3_006', {'weight': 18726.0}),
     ('ISBH3F3_007', 'ISBH3F3_007', {'weight': 26800.0}),
     ('ISBH3F3_009', 'ISBH3F3_009', {'weight': 18878.0}),
     ('ISBH3F3_010', 'ISBH3F3_010', {'weight': 9410.0}),
     ('ISBH3F3_011', 'ISBH3F3_011', {'weight': 16343.0}),
     ('ISBH3F3_013', 'PAL1D4_016', {'weight': 7455.0}),
     ('PAL1D4_016', 'PAB3F5_008', {'weight': 9876.0}),
     ('PAL1D4_016', 'PAL1D4_016', {'weight': 7219.0}),
     ('PAL1D4_016', 'PAL0A1_020', {'weight': 6177.0}),
     ('JHB0A2_003', 'JHB0A2_003', {'weight': 24533.0}),
     ('PNG3F7_005', 'PNG3F7_005', {'weight': 5060.0}),
     ('PNG3F7_005', 'PNG3F7_005', {'weight': 7439.0}),
     ('JHB0A2_005', 'JHB0A2_005', {'weight': 13396.0}),
     ('JHB0A2_006', 'PAL1D4_028', {'weight': 5002.0}),
     ('PAL1D4_028', 'PAL0A1_006', {'weight': 5577.0}),
     ('PAL1D4_028', 'PAL1D4_028', {'weight': 10824.0}),
     ('JHB0A2_019', 'JHB0A2_019', {'weight': 8890.0}),
     ('JHB0A2_019', 'JHB0A2_019', {'weight': 9166.0}),
     ('JHB0A2_019', 'PNG3F7_016', {'weight': 10062.0}),
     ('PNG3F7_016', 'PNG3F7_016', {'weight': 38864.0}),
     ('PNG3F7_016', 'PNG0A4_002', {'weight': 17622.0}),
     ('JHB0A2_021', 'JHB0A2_021', {'weight': 16260.0}),
     ('JHB0A2_025', 'JHB0A2_025', {'weight': 9892.0}),
     ('JHB0A2_027', 'JHB0A2_027', {'weight': 10494.0}),
     ('JHB0A2_027', 'PAL0A1_026', {'weight': 7016.0}),
     ('JHB0A2_027', 'PAL0A1_026', {'weight': 7018.0}),
     ('PAL0A1_026', 'PAL0A1_026', {'weight': 10395.0}),
     ('JHB0A2_030', 'JHB0A2_030', {'weight': 14827.0}),
     ('JHB0A2_030', 'PAL0A1_029', {'weight': 11230.0}),
     ('JHB0A2_030', 'PAL0A1_029', {'weight': 11292.0}),
     ('PAL0A1_029', 'PAL0A1_029', {'weight': 16037.0}),
     ('JHB0A2_031', 'JHB0A2_031', {'weight': 22218.0}),
     ('JHB0A2_033', 'JHB0A2_033', {'weight': 23720.0}),
     ('PAL0A1_033', 'PAL0A1_033', {'weight': 77222.0}),
     ('PAL0A1_033', 'PNG0A4_026', {'weight': 20705.0}),
     ('PAL0A1_033', 'PNG0A4_026', {'weight': 25394.0}),
     ('PAL0A1_033', 'PAL1D4_011', {'weight': 10688.0}),
     ('JHB0A2_038', 'JHB0A2_038', {'weight': 22865.0}),
     ('NAK4C8_002', 'NAK4C8_002', {'weight': 37399.0}),
     ('NAK4C8_003', 'NAK4C8_003', {'weight': 12952.0}),
     ('NAK4C8_006', 'NAK4C8_006', {'weight': 7314.0}),
     ('PAB3F5_001', 'PAB3F5_001', {'weight': 29092.0}),
     ('PAB3F5_004', 'PAB3F5_004', {'weight': 27134.0}),
     ('PAB3F5_005', 'PAB3F5_005', {'weight': 17347.0}),
     ('PAB3F5_006', 'PAB3F5_006', {'weight': 7258.0}),
     ('PAB3F5_007', 'PNG3F7_025', {'weight': 6984.0}),
     ('PNG3F7_025', 'PNG3F7_025', {'weight': 11152.0}),
     ('PAB3F5_009', 'PNG3F7_027', {'weight': 7745.0}),
     ('PNG3F7_027', 'PNG3F7_027', {'weight': 5207.0}),
     ('PNG3F7_027', 'PNG0A4_004', {'weight': 5072.0}),
     ('PAB3F5_011', 'PAB3F5_011', {'weight': 6321.0}),
     ('PAL0A1_001', 'PAL0A1_001', {'weight': 19898.0}),
     ('PAL0A1_001', 'PAL1D4_032', {'weight': 7602.0}),
     ('PAL0A1_002', 'PAL0A1_002', {'weight': 5085.0}),
     ('PNG0A4_002', 'PNG0A4_002', {'weight': 27277.0}),
     ('PAL0A1_011', 'PAL0A1_011', {'weight': 28687.0}),
     ('PAL0A1_011', 'PNG0A4_011', {'weight': 17054.0}),
     ('PAL0A1_011', 'PNG0A4_011', {'weight': 17033.0}),
     ('PAL0A1_011', 'PAL1D4_007', {'weight': 7273.0}),
     ('PNG0A4_011', 'PNG0A4_011', {'weight': 22196.0}),
     ('PNG0A4_011', 'PNG3F7_021', {'weight': 14568.0}),
     ('PNG0A4_011', 'PNG3F7_021', {'weight': 14527.0}),
     ('PAL0A1_013', 'PAL0A1_013', {'weight': 5188.0}),
     ('PAL0A1_013', 'PAL0A1_013', {'weight': 29400.0}),
     ('PAL0A1_013', 'PAL1D4_015', {'weight': 7282.0}),
     ('PAL0A1_013', 'PAL1D4_015', {'weight': 17194.0}),
     ('PAL0A1_017', 'PAL0A1_017', {'weight': 28829.0}),
     ('PAL0A1_017', 'PAL1D4_034', {'weight': 5053.0}),
     ('PAL0A1_020', 'PAL0A1_020', {'weight': 24027.0}),
     ('PNG3F7_013', 'PNG3F7_013', {'weight': 8211.0}),
     ('PAL0A1_023', 'PAL0A1_023', {'weight': 11479.0}),
     ('PAL0A1_023', 'PNG0A4_018', {'weight': 6357.0}),
     ('PAL0A1_023', 'PNG3F7_017', {'weight': 5504.0}),
     ('PAL0A1_030', 'PAL0A1_030', {'weight': 10805.0}),
     ('PAL0A1_030', 'PNG3F7_009', {'weight': 8653.0}),
     ('PAL0A1_030', 'PNG3F7_009', {'weight': 8568.0}),
     ('PAL0A1_030', 'PAL1D4_036', {'weight': 5620.0}),
     ('PAL0A1_030', 'PAL1D4_036', {'weight': 5610.0}),
     ('PNG3F7_009', 'PAL1D4_036', {'weight': 5330.0}),
     ('PNG3F7_009', 'PAL1D4_036', {'weight': 5341.0}),
     ('PNG3F7_009', 'PAP1D6_005', {'weight': 24867.0}),
     ('PNG3F7_009', 'PNG3F7_009', {'weight': 12856.0}),
     ('PAL1D4_036', 'PAL1D4_036', {'weight': 5503.0}),
     ('PNG0A4_025', 'PNG0A4_025', {'weight': 18350.0}),
     ('PNG0A4_026', 'PNG0A4_026', {'weight': 25788.0}),
     ('PAL1D4_009', 'PAL1D4_009', {'weight': 16058.0}),
     ('PAL1D4_020', 'PAL1D4_020', {'weight': 5289.0}),
     ('PAL0A1_039', 'PAL0A1_039', {'weight': 10101.0}),
     ('PAL0A1_040', 'PAL0A1_040', {'weight': 10326.0}),
     ('PAL1D4_001', 'PAL1D4_001', {'weight': 32542.0}),
     ('PAL1D4_006', 'PAL1D4_006', {'weight': 9321.0}),
     ('PAL1D4_007', 'PAL1D4_007', {'weight': 7273.0}),
     ('PAL1D4_011', 'PAL1D4_011', {'weight': 7507.0}),
     ('PAL1D4_011', 'PNG3F7_019', {'weight': 5152.0}),
     ('PAL1D4_013', 'PAL1D4_013', {'weight': 12588.0}),
     ('PAL1D4_015', 'PAL1D4_015', {'weight': 7419.0}),
     ('PAL1D4_015', 'PAL1D4_015', {'weight': 16259.0}),
     ('PAL1D4_017', 'PAL1D4_017', {'weight': 7716.0}),
     ('PAL1D4_022', 'PAL1D4_022', {'weight': 13156.0}),
     ('PNG3F7_010', 'PNG3F7_010', {'weight': 16902.0}),
     ('PAL1D4_024', 'PAL1D4_024', {'weight': 12083.0}),
     ('PAL1D4_025', 'PAL1D4_025', {'weight': 6372.0}),
     ('PAL1D4_025', 'PAL1D4_025', {'weight': 6115.0}),
     ('PAL1D4_031', 'PAL1D4_031', {'weight': 8879.0}),
     ('PAL1D4_031', 'PNG0A4_015', {'weight': 6374.0}),
     ('PAL1D4_031', 'PNG0A4_015', {'weight': 6374.0}),
     ('PAL1D4_031', 'PNG3F7_018', {'weight': 6315.0}),
     ('PNG0A4_015', 'PNG0A4_015', {'weight': 12061.0}),
     ('PNG0A4_015', 'PNG3F7_018', {'weight': 7187.0}),
     ('PNG3F7_018', 'PNG3F7_018', {'weight': 10205.0}),
     ('PAL1D4_032', 'PAL1D4_032', {'weight': 7600.0}),
     ('PAL1D4_033', 'PAL1D4_033', {'weight': 5593.0}),
     ('PAL1D4_033', 'PAL1D4_033', {'weight': 6934.0}),
     ('PAL1D4_034', 'PAP1D6_013', {'weight': 5049.0}),
     ('PAP1D6_013', 'PAP1D6_013', {'weight': 6797.0}),
     ('PAP1D6_002', 'PAP1D6_002', {'weight': 11669.0}),
     ('PAP1D6_004', 'PAP1D6_004', {'weight': 25650.0}),
     ('PAP1D6_006', 'PAP1D6_006', {'weight': 9427.0}),
     ('PAP1D6_007', 'PAP1D6_007', {'weight': 11070.0}),
     ('PAP1D6_010', 'PAP1D6_010', {'weight': 16316.0}),
     ('PAP1D6_012', 'PAP1D6_012', {'weight': 12484.0}),
     ('PAP1D6_014', 'PAP1D6_014', {'weight': 7051.0}),
     ('PAP1D6_015', 'PAP1D6_015', {'weight': 6036.0}),
     ('PNG0A4_001', 'PNG0A4_001', {'weight': 5135.0}),
     ('PNG0A4_004', 'PNG0A4_004', {'weight': 20731.0}),
     ('PNG0A4_008', 'PNG0A4_008', {'weight': 23273.0}),
     ('PNG0A4_010', 'PNG0A4_010', {'weight': 8356.0}),
     ('PNG3F7_021', 'PNG3F7_021', {'weight': 19350.0}),
     ('PNG0A4_013', 'PNG0A4_013', {'weight': 29758.0}),
     ('PNG0A4_017', 'PNG0A4_017', {'weight': 9148.0}),
     ('PNG0A4_018', 'PNG0A4_018', {'weight': 10016.0}),
     ('PNG0A4_018', 'PNG3F7_017', {'weight': 5436.0}),
     ('PNG0A4_021', 'PNG0A4_021', {'weight': 11455.0}),
     ('PNG0A4_023', 'PNG0A4_023', {'weight': 36963.0}),
     ('PNG0A4_024', 'PNG0A4_024', {'weight': 21270.0}),
     ('PNG0A4_028', 'PNG0A4_028', {'weight': 25804.0}),
     ('PNG0A4_029', 'PNG0A4_029', {'weight': 5271.0}),
     ('PNG0A4_031', 'PNG0A4_031', {'weight': 5928.0}),
     ('PNG3F7_008', 'PNG3F7_008', {'weight': 5427.0}),
     ('PNG3F7_012', 'PNG3F7_012', {'weight': 8196.0}),
     ('PNG3F7_015', 'PNG3F7_015', {'weight': 11268.0}),
     ('PNG3F7_017', 'PNG3F7_017', {'weight': 9249.0}),
     ('PNG3F7_022', 'PNG3F7_022', {'weight': 8579.0}),
     ('PNG3F7_026', 'PNG3F7_026', {'weight': 11848.0}),
     ('STM4C5_001', 'STM4C5_001', {'weight': 43879.0}),
     ('STM4C5_002', 'STM4C5_002', {'weight': 12144.0}),
     ('STM4C5_005', 'STM4C5_005', {'weight': 13696.0}),
     ('STM4C5_007', 'STM4C5_007', {'weight': 7302.0}),
     ('STM4C5_008', 'STM4C5_008', {'weight': 6422.0}),
     ('STM4C5_009', 'STM4C5_009', {'weight': 12208.0}),
     ('STM4C5_010', 'STM4C5_010', {'weight': 7481.0}),
     ('STM4C5_012', 'STM4C5_012', {'weight': 5290.0})]




```python
nx.draw(G)
plt.draw()
plt.show()
```

    /Users/jasonblues/anaconda/lib/python3.6/site-packages/networkx/drawing/nx_pylab.py:126: MatplotlibDeprecationWarning: pyplot.hold is deprecated.
        Future behavior will be consistent with the long-time default:
        plot commands add elements without first clearing the
        Axes and/or Figure.
      b = plt.ishold()
    /Users/jasonblues/anaconda/lib/python3.6/site-packages/networkx/drawing/nx_pylab.py:138: MatplotlibDeprecationWarning: pyplot.hold is deprecated.
        Future behavior will be consistent with the long-time default:
        plot commands add elements without first clearing the
        Axes and/or Figure.
      plt.hold(b)
    /Users/jasonblues/anaconda/lib/python3.6/site-packages/matplotlib/__init__.py:917: UserWarning: axes.hold is deprecated. Please remove it from your matplotlibrc and/or style files.
      warnings.warn(self.msg_depr_set % key)
    /Users/jasonblues/anaconda/lib/python3.6/site-packages/matplotlib/rcsetup.py:152: UserWarning: axes.hold is deprecated, will be removed in 3.0
      warnings.warn("axes.hold is deprecated, will be removed in 3.0")



![png](output_2_1.png)



```python
families = list(nx.connected_component_subgraphs(G))
```


```python
nx.draw(families[4])
plt.draw()
plt.show()
families[4].nodes()
```

    /Users/jasonblues/anaconda/lib/python3.6/site-packages/networkx/drawing/nx_pylab.py:126: MatplotlibDeprecationWarning: pyplot.hold is deprecated.
        Future behavior will be consistent with the long-time default:
        plot commands add elements without first clearing the
        Axes and/or Figure.
      b = plt.ishold()
    /Users/jasonblues/anaconda/lib/python3.6/site-packages/networkx/drawing/nx_pylab.py:138: MatplotlibDeprecationWarning: pyplot.hold is deprecated.
        Future behavior will be consistent with the long-time default:
        plot commands add elements without first clearing the
        Axes and/or Figure.
      plt.hold(b)
    /Users/jasonblues/anaconda/lib/python3.6/site-packages/matplotlib/__init__.py:917: UserWarning: axes.hold is deprecated. Please remove it from your matplotlibrc and/or style files.
      warnings.warn(self.msg_depr_set % key)
    /Users/jasonblues/anaconda/lib/python3.6/site-packages/matplotlib/rcsetup.py:152: UserWarning: axes.hold is deprecated, will be removed in 3.0
      warnings.warn("axes.hold is deprecated, will be removed in 3.0")



![png](output_4_1.png)





    ['3L0A3_011',
     'ASI1E3_006',
     'GL890823',
     'PAL1D4_019',
     'PNG0A4_012',
     'JHB0A2_016',
     '3L0A3_010',
     'PAL0A1_012']




```python
print(len(families))
```

    137



```python
families[60].nodes()

```




    ['ISBH3F3_003', 'CHN1D9_002']




```python
toremove=[]
for family in families:
    if len(family.nodes()) == 1:
        toremove.append(family)
len(toremove)
    
```




    92




```python
for fm in toremove:
    families.remove(fm)
len(families)
```




    45




```python
bgcs={}
with open('/Users/jasonblues/Desktop/Project_files/bgcs.txt','r') as nodes:
    for node in nodes:
        infopair = node.split('\t')
        bgcs[infopair[0]] = infopair[1]
        print(infopair[1])
        
#        if infopair[1] in Strains:
#            Strains[infopair[1]].append(infopair[0])
#        else:
#            li = [infopair[0]]
#            Strains[infopair[1]] = li
nodes.close()

```

    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    Ga0081465_101 Moorea producens-heterotrophic bacteria co-culture from Cura?ao Moorea producens 3L (One linear chromosome and 78 unmapped contigs) : Ga0081465_101
    
    NODE_1_length_301640_cov_23.3452
    
    NODE_2_length_271752_cov_22.5019
    
    NODE_5_length_207573_cov_23.5248
    
    NODE_6_length_206503_cov_22.5354
    
    NODE_9_length_169776_cov_22.971
    
    NODE_9_length_169776_cov_22.971
    
    NODE_10_length_168169_cov_23.0888
    
    NODE_11_length_164926_cov_23.8494
    
    NODE_11_length_164926_cov_23.8494
    
    NODE_12_length_164389_cov_23.5503
    
    NODE_15_length_142369_cov_22.3646
    
    NODE_17_length_140822_cov_23.6252
    
    NODE_17_length_140822_cov_23.6252
    
    NODE_18_length_134738_cov_23.6809
    
    NODE_19_length_126487_cov_22.9518
    
    NODE_20_length_125298_cov_24.1806
    
    NODE_21_length_124012_cov_23.1389
    
    NODE_23_length_118440_cov_23.5909
    
    NODE_26_length_111257_cov_22.3537
    
    NODE_30_length_100068_cov_24.2634
    
    NODE_33_length_97375_cov_25.5465
    
    NODE_33_length_97375_cov_25.5465
    
    NODE_34_length_95516_cov_23.174
    
    NODE_35_length_94889_cov_22.8329
    
    NODE_37_length_94532_cov_22.8489
    
    NODE_41_length_87340_cov_22.4049
    
    NODE_42_length_87197_cov_22.658
    
    NODE_47_length_79879_cov_22.0611
    
    NODE_48_length_79779_cov_24.1753
    
    NODE_49_length_79440_cov_23.094
    
    NODE_49_length_79440_cov_23.094
    
    NODE_52_length_73656_cov_22.905
    
    NODE_54_length_73275_cov_22.4413
    
    NODE_2_length_1226009_cov_13.0042
    
    NODE_2_length_1226009_cov_13.0042
    
    NODE_3_length_1133679_cov_25.0191
    
    NODE_3_length_1133679_cov_25.0191
    
    NODE_3_length_1133679_cov_25.0191
    
    NODE_4_length_1000275_cov_25.4078
    
    NODE_4_length_1000275_cov_25.4078
    
    NODE_4_length_1000275_cov_25.4078
    
    NODE_7_length_585882_cov_43.3162
    
    NODE_7_length_585882_cov_43.3162
    
    NODE_7_length_585882_cov_43.3162
    
    NODE_8_length_556756_cov_24.8745
    
    NODE_9_length_504326_cov_25.6874
    
    NODE_9_length_504326_cov_25.6874
    
    NODE_12_length_278909_cov_12.1341
    
    NODE_12_length_278909_cov_12.1341
    
    NODE_13_length_270747_cov_11.9165
    
    NODE_15_length_218209_cov_25.4862
    
    NODE_16_length_217052_cov_25.5719
    
    NODE_19_length_203773_cov_12.6272
    
    NODE_20_length_197242_cov_24.8251
    
    NODE_23_length_170518_cov_26.1373
    
    NODE_26_length_148424_cov_24.4653
    
    NODE_26_length_148424_cov_24.4653
    
    NODE_32_length_114599_cov_24.2633
    
    NODE_38_length_87221_cov_25.7119
    
    NODE_42_length_66227_cov_25.4789
    
    NODE_43_length_64961_cov_26.278
    
    NODE_55_length_41904_cov_26.3835
    
    NODE_316_length_4019_cov_3.36228
    
    NODE_515_length_3379_cov_3.05258
    
    NODE_857_length_2778_cov_3.82988
    
    NODE_8_length_68275_cov_17.2667
    
    NODE_15_length_56212_cov_16.216
    
    NODE_23_length_47501_cov_16.84
    
    NODE_30_length_44373_cov_17.9269
    
    NODE_49_length_36261_cov_15.9889
    
    NODE_51_length_35746_cov_16.2317
    
    NODE_53_length_35490_cov_15.589
    
    NODE_55_length_33250_cov_16.0127
    
    NODE_71_length_27518_cov_17.1009
    
    NODE_79_length_26416_cov_16.5965
    
    NODE_81_length_26125_cov_15.6505
    
    NODE_87_length_24102_cov_16.147
    
    NODE_106_length_21327_cov_17.3724
    
    NODE_119_length_19670_cov_14.1459
    
    NODE_122_length_18806_cov_16.0237
    
    NODE_131_length_17253_cov_16.7547
    
    NODE_174_length_11660_cov_16.8796
    
    NODE_249_length_5760_cov_17.2487
    
    NODE_309_length_3197_cov_13.6176
    
    NODE_10_length_89053_cov_4.61339
    
    NODE_11_length_87862_cov_4.65999
    
    NODE_15_length_82885_cov_4.6418
    
    NODE_22_length_66858_cov_4.99023
    
    NODE_26_length_63757_cov_5.17971
    
    NODE_66_length_41655_cov_4.89227
    
    NODE_74_length_38571_cov_5.64234
    
    NODE_78_length_35930_cov_5.48261
    
    NODE_90_length_31891_cov_5.12757
    
    NODE_97_length_29601_cov_4.99573
    
    NODE_98_length_29313_cov_4.09871
    
    NODE_100_length_29021_cov_5.25178
    
    NODE_123_length_23438_cov_5.3923
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    Ga0081187_11 Moorea producens-heterotrophic bacteria co-culture from Jamaica Moorea producens JHB 22AUG96-1 (Final Draft of Linear Chromosome and 2 Linear Plasmid Scaffolds) : Ga0081187_11
    
    NODE_1_length_1491099_cov_33.8025
    
    NODE_1_length_1491099_cov_33.8025
    
    NODE_3_length_696822_cov_33.6907
    
    NODE_23_length_41122_cov_6.50799
    
    NODE_292_length_11655_cov_3.51856
    
    NODE_687_length_7447_cov_4.98347
    
    NODE_700_length_7357_cov_5.06902
    
    NODE_753_length_7053_cov_3.52166
    
    NODE_759_length_7015_cov_5.9158
    
    NODE_942_length_6288_cov_4.50381
    
    NODE_5_length_131820_cov_20.0334
    
    NODE_11_length_98022_cov_19.2876
    
    NODE_26_length_63270_cov_18.4583
    
    NODE_40_length_51162_cov_19.7772
    
    NODE_72_length_29914_cov_34.4195
    
    NODE_92_length_24021_cov_24.5842
    
    NODE_111_length_19560_cov_33.1062
    
    NODE_123_length_17063_cov_19.3075
    
    NODE_144_length_12963_cov_22.4381
    
    NODE_174_length_9569_cov_24.2438
    
    NODE_229_length_5697_cov_28.5433
    
    NODE_430_length_3184_cov_2.31142
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    Chromosome_contig_1_Moorea_producens_PAL_15AUG08-1
    
    NODE_1_length_1975226_cov_28.3546
    
    NODE_17_length_120728_cov_8.6785
    
    NODE_38_length_65444_cov_7.43662
    
    NODE_41_length_61260_cov_7.43513
    
    NODE_47_length_55640_cov_8.82622
    
    NODE_48_length_55545_cov_8.48556
    
    NODE_56_length_51160_cov_7.90034
    
    NODE_64_length_49335_cov_6.98622
    
    NODE_77_length_45375_cov_7.11326
    
    NODE_87_length_41464_cov_6.89065
    
    NODE_91_length_39969_cov_7.21811
    
    NODE_98_length_38191_cov_8.29419
    
    NODE_102_length_36637_cov_6.63728
    
    NODE_117_length_33645_cov_7.06423
    
    NODE_118_length_33361_cov_8.22964
    
    NODE_123_length_32389_cov_7.21766
    
    NODE_132_length_31363_cov_7.56928
    
    NODE_146_length_29377_cov_6.45997
    
    NODE_147_length_28694_cov_7.30906
    
    NODE_161_length_27817_cov_6.31203
    
    NODE_166_length_27377_cov_7.4429
    
    NODE_198_length_23828_cov_7.85326
    
    NODE_199_length_23792_cov_6.90137
    
    NODE_227_length_21836_cov_7.85283
    
    NODE_231_length_21440_cov_7.61531
    
    NODE_241_length_20666_cov_7.12264
    
    NODE_242_length_20629_cov_6.62965
    
    NODE_244_length_20395_cov_7.39821
    
    NODE_251_length_19791_cov_7.24593
    
    NODE_287_length_17644_cov_8.11201
    
    NODE_290_length_17495_cov_7.27182
    
    NODE_320_length_15970_cov_6.4977
    
    NODE_341_length_15258_cov_7.99696
    
    NODE_343_length_15083_cov_7.22299
    
    NODE_349_length_14926_cov_5.55071
    
    NODE_374_length_13805_cov_6.87381
    
    NODE_376_length_13754_cov_7.53218
    
    NODE_1_length_1155603_cov_20.2601
    
    NODE_2_length_901746_cov_19.7973
    
    NODE_9_length_216945_cov_22.8205
    
    NODE_16_length_130316_cov_22.8508
    
    NODE_28_length_86537_cov_22.3555
    
    NODE_37_length_60587_cov_7.50119
    
    NODE_48_length_52418_cov_6.55878
    
    NODE_65_length_42869_cov_6.71988
    
    NODE_66_length_42764_cov_6.69285
    
    NODE_137_length_28174_cov_6.02346
    
    NODE_201_length_23662_cov_5.66743
    
    NODE_246_length_21046_cov_7.60921
    
    NODE_343_length_17167_cov_7.18275
    
    NODE_571_length_12513_cov_6.43299
    
    NODE_798_length_9934_cov_6.7565
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    Ga0081470_101 Moorea bouillonii-heterotrophic bacteria co-culture from Papua New Guinea Moorea bouillonii PNG 19MAY05-8 (One linear chromosome and 12 unmapped contigs) : Ga0081470_101
    
    NODE_1_length_202734_cov_11.1468
    
    NODE_3_length_127219_cov_11.5549
    
    NODE_11_length_95623_cov_12.4329
    
    NODE_12_length_90842_cov_11.0778
    
    NODE_19_length_73395_cov_11.3741
    
    NODE_25_length_68229_cov_11.4173
    
    NODE_27_length_65968_cov_11.3237
    
    NODE_28_length_65258_cov_10.9639
    
    NODE_29_length_65213_cov_11.0117
    
    NODE_30_length_64084_cov_11.2848
    
    NODE_38_length_59954_cov_11.3618
    
    NODE_39_length_59110_cov_11.5385
    
    NODE_41_length_56899_cov_11.6275
    
    NODE_44_length_53279_cov_11.2149
    
    NODE_47_length_51145_cov_11.0767
    
    NODE_64_length_41655_cov_11.0148
    
    NODE_67_length_39780_cov_10.8023
    
    NODE_70_length_39124_cov_11.4581
    
    NODE_73_length_38563_cov_11.2891
    
    NODE_76_length_37295_cov_11.1242
    
    NODE_78_length_36869_cov_11.7963
    
    NODE_87_length_34762_cov_11.9151
    
    NODE_93_length_32386_cov_11.0608
    
    NODE_111_length_27211_cov_11.0384
    
    NODE_141_length_18898_cov_12.0126
    
    NODE_144_length_17993_cov_11.7726
    
    NODE_158_length_16072_cov_11.1904
    
    NODE_225_length_9385_cov_10.6631
    
    NODE_233_length_8901_cov_47.4889
    
    NODE_259_length_7259_cov_2.55609
    
    NODE_260_length_7257_cov_11.4337
    
    NODE_339_length_5406_cov_1.89638
    
    NODE_344_length_5339_cov_2.36838
    
    NODE_356_length_5272_cov_11.6422
    
    NODE_450_length_4345_cov_10.666
    
    NODE_457_length_4279_cov_11.7389
    
    NODE_6_length_58891_cov_15.6902
    
    NODE_9_length_45013_cov_10.0725
    
    NODE_11_length_44484_cov_10.1958
    
    NODE_26_length_27730_cov_10.1873
    
    NODE_54_length_22032_cov_10.6252
    
    NODE_67_length_19349_cov_9.20544
    
    NODE_84_length_16825_cov_8.09157
    
    NODE_109_length_14902_cov_7.61313
    
    NODE_115_length_14535_cov_8.75236
    
    NODE_139_length_13203_cov_7.92559
    
    NODE_262_length_9315_cov_11.7337
    
    NODE_397_length_7191_cov_5.1301
    
    NODE_415_length_6978_cov_4.46168
    
    NODE_463_length_6458_cov_6.12273
    
    NODE_771_length_4488_cov_8.68769
    
    NODE_857_length_4054_cov_4.67176
    
    Nostoc sp. ATCC 53789
    
    Nostoc sp. ATCC 53789
    
    Lyngbya majuscula
    
    Planktothrix agardhii NIVA-CYA 116
    
    Arabidopsis thaliana
    
    Moorea producens 3L
    
    Moorea producens JHB
    
    Moorea bouillonii PNG5-198
    
    Cylindrospermum alatosporum CCALA 988
    
    Streptomyces nodosus subsp. asukaensis
    
    Lyngbya majuscula
    
    Moorea producens 3L
    
    Planktothrix agardhii NIVA-CYA 126
    
    Anabaena sp. 90
    
    Candidatus Entotheonella sp. (ex. Theonella swinhoei)
    
    Planktothrix agardhii NIVA-CYA 126/8
    
    Anabaena sp. 90
    
    Heliobacillus mobilis
    
    Heliophilum fasciatum
    
    Microcystis aeruginosa NIES-98
    
    Lyngbya majuscula
    
    Nostoc sp. 152
    
    Nostoc sp. CAVN2
    
    Cylindrospermum licheniforme UTEX B 2014
    
    Methylobacter marinus
    
    Sporosarcina pasteurii
    
    Methylomicrobium kenyense
    
    Methylophaga alcalica
    
    Methylomicrobium alcaliphilum
    
    Methylomicrobium alcaliphilum 20Z
    
    Cylindrospermopsis raciborskii AWT205
    
    Aphanizomenon sp. 10E6
    
    Planktothrix agardhii NIES-596
    
    Trichodesmium erythraeum IMS101
    
    Microcystis aeruginosa PCC 7005
    
    uncultured Prochloron sp. 06037A
    
    Sphingomonas sp. PB304
    
    Sorangium cellulosum
    
    Chondromyces crocatus
    
    Streptoalloteichus sp. ATCC 53650
    
    Sorangium cellulosum
    
    Nostoc punctiforme PCC 73102
    
    Lyngbya majuscula
    
    Sorangium cellulosum
    
    Sorangium cellulosum
    
    Sorangium cellulosum So0157-2
    
    Sorangium cellulosum
    
    Moorea producens 19L
    
    Methylophaga thalassica
    
    Actinomadura kijaniata
    
    Microcystis aeruginosa K-139
    
    Microcystis sp. NIVA-CYA 172/5
    
    Stigmatella aurantiaca Sg a15
    
    Nocardiopsis sp. TFS65-07
    
    Bacillus cereus ATCC 14579
    
    Algoriphagus sp. KK10202C
    
    Nostoc sp. 'Peltigera membranacea cyanobiont'
    
    Chondromyces crocatus
    
    Stigmatella aurantiaca
    
    Anabaena variabilis ATCC 29413
    
    [Oscillatoria] sp. PCC 6506
    
    Rhodobacter sphaeroides
    
    Streptomyces halstedii
    
    Escherichia coli
    
    Anabaena sp. Syke748
    
    Streptomyces sp. KCTC 0041BP
    
    Streptomyces bikiniensis
    
    Streptomyces sp. A1(2016)
    



```python
strain_list = []
for f in families:
    nl = f.nodes()
    for bgc in nl:

        if bgc.find('_') != -1:
            nomen = bgc.split('_')
            if nomen[0] in strain_list:
                print("in here already")
            else:
                strain_list.append(nomen[0])
                print(nomen[0])
```

    JHB0A2
    ASI1E3
    in here already
    PAL1D4
    NAK4C8
    3L0A3
    PNG0A4
    in here already
    PNG3F7
    PAL0A1
    PAP1D6
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    ASX1E4
    in here already
    in here already
    CHN1D9
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    ISBH3F3
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    PAB3F5
    STM4C5
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already
    in here already



```python
len(strain_list)
```




    14




```python
p_axis = []
for strain in strain_list:
    otu = []
    for fami in families: 
        edges = fami.edges(data=True)
        idnt = 0
        avg = 1
        for edge in edges:
            if edge[0].split('_')[0] == strain:
                idnt = idnt + int(edge[2]['weight'])
        otu.append(int(idnt/avg))
    p_axis.append(otu)
                
```


```python
import numpy as np
print(np.matrix(p_axis))
```

    [[105069      0  24641  22095   5620 144662  14876      0   6786   9837
       25350  46753      0      0      0      0      0      0      0      0
       30814   6141   8621  20062      0      0      0  84876      0  52673
           0      0      0      0      0  24528  37349      0      0      0
           0      0      0      0      0]
     [ 92668      0   9377  14426  17840 111959      0      0      0      0
           0   6651      0      0      0      0      0      0      0      0
           0  15036      0      0      0  28838      0  48287      0  23490
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0]
     [ 97699      0  28832      0  11940  81358   7716      0      0      0
           0      0      0      0  12659      0  32873      0      0      0
           0      0  15341  44788  14337   5289  39762      0      0  25395
           0      0      0      0  23272      0      0      0      0  15202
       14546      0      0  27404  15194]
     [ 43444      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0  64192      0      0      0      0      0      0
           0      0      0      0      0]
     [118350      0  37202  22853  44748      0      0   7239  23545   6507
           0      0      0      0      0      0      0      0      0      0
       18938  21581  23392  59350  21871  54296      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0]
     [138814      0      0      0  12752 100735      0      0      0      0
           0      0      0      0  25788      0      0      0      0      0
           0  27245  64898  18350      0      0      0  69419      0      0
           0      0      0      0      0      0      0      0  25803      0
       56283      0  10016      0  31996]
     [152250      0      0      0      0  95903  47762      0      0      0
           0  19355      0      0      0      0      0      0      0      0
           0  74378      0      0      0      0      0      0  17007      0
           0      0      0      0      0      0      0  11152   5207      0
       48445      0  20189  12856  10205]
     [199064      0  46690      0  41951  92838      0      0      0  12085
           0 153078      0      0 181793      0      0      0      0      0
           0  14893  48365  18996  12691 120739  34698  29368      0  33575
           0      0      0      0  24027  10395  16037      0      0  19898
       28687  33882  17836  28026      0]
     [ 32748      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0  31875
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0  11846      0  24867      0]
     [     0      0      0      0      0      0      0      0      0      0
           0      0   5050  11372      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0  18374      0      0      0      0      0      0      0      0
           0      0      0      0      0]
     [     0      0      0      0      0   9965      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
       37424      0      0      0      0      0      0      0      0      0
           0      0      0      0      0]
     [     0      0      0      0      0  85298      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0  22639      0      0
           0      0  46918   5350   7455      0      0      0      0      0
           0      0      0      0      0]
     [     0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0  11665      0      0      0      0      0   6984   7745      0
           0      0      0      0      0]
     [     0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0      0      0      0      0      0      0      0      0      0
           0  16758      0  21128      0      0      0      0      0      0
           0      0      0      0      0]]



```python
for la in strain_list:
    print(la)
```

    JHB0A2
    ASI1E3
    PAL1D4
    NAK4C8
    3L0A3
    PNG0A4
    PNG3F7
    PAL0A1
    PAP1D6
    ASX1E4
    CHN1D9
    ISBH3F3
    PAB3F5
    STM4C5



```python
from skbio.diversity import beta_diversity
bc_dm = beta_diversity("braycurtis", p_axis, strain_list)
print(bc_dm)
```

    14x14 distance matrix
    IDs:
    'JHB0A2', 'ASI1E3', 'PAL1D4', 'NAK4C8', '3L0A3', 'PNG0A4', 'PNG3F7', 'PAL0A1', ...
    Data:
    [[ 0.          0.38687321  0.54217974  0.88837458  0.60290989  0.4988155
       0.5928271   0.56845265  0.9151704   1.          0.97224783  0.74252069
       1.          1.        ]
     [ 0.38687321  0.          0.49188997  0.81754191  0.56983212  0.43307832
       0.52391595  0.60210782  0.86061953  1.          0.95208685  0.59742425
       1.          1.        ]
     [ 0.54217974  0.49188997  0.          0.86013846  0.55165751  0.51248419
       0.56359718  0.50921147  0.81261678  1.          0.9644739   0.73927109
       1.          1.        ]
     [ 0.88837458  0.81754191  0.86013846  0.          0.84689555  0.87402698
       0.86038612  0.93453522  0.68658002  1.          1.          0.96113274
       1.          0.70962466]
     [ 0.60290989  0.56983212  0.55165751  0.84689555  0.          0.62681303
       0.71283865  0.60907279  0.88329461  1.          1.          1.          1.
       1.        ]
     [ 0.4988155   0.43307832  0.51248419  0.87402698  0.62681303  0.
       0.38761388  0.5339197   0.90416645  1.          0.96833935  0.71207548
       0.97454367  1.        ]
     [ 0.5928271   0.52391595  0.56359718  0.86038612  0.71283865  0.38761388
       0.          0.60939757  0.85194588  1.          0.96454355  0.7499945
       0.95494019  1.        ]
     [ 0.56845265  0.60210782  0.50921147  0.93453522  0.60907279  0.5339197
       0.60939757  0.          0.89483159  1.          0.98426994  0.83364185
       1.          1.        ]
     [ 0.9151704   0.86061953  0.81261678  0.68658002  0.88329461  0.90416645
       0.85194588  0.89483159  0.          1.          1.          1.          1.
       1.        ]
     [ 1.          1.          1.          1.          1.          1.          1.
       1.          1.          0.          1.          1.          0.61872855
       0.53886795]
     [ 0.97224783  0.95208685  0.9644739   1.          1.          0.96833935
       0.96454355  0.98426994  1.          1.          0.          0.90732345
       1.          1.        ]
     [ 0.74252069  0.59742425  0.73927109  0.96113274  1.          0.71207548
       0.7499945   0.83364185  1.          1.          0.90732345  0.          1.
       0.94794353]
     [ 1.          1.          1.          1.          1.          0.97454367
       0.95494019  1.          1.          0.61872855  1.          1.          0.
       0.63705663]
     [ 1.          1.          1.          0.70962466  1.          1.          1.
       1.          1.          0.53886795  1.          0.94794353  0.63705663
       0.        ]]



```python
from skbio.stats.ordination import pcoa
bc_pc = pcoa(bc_dm)
```


```python
import pandas as pd
```


```python
sample_md = [('PAL0A1', ['Moorea']),('PAL1D4', ['Moorea']),('JHB0A2', ['Moorea']),('NAK4C8', ['Okeania']),('3L0A3', ['Moorea']),('ASI1E3', ['Moorea']),('ASX1E4', ['Leptolyngbya']),('PNG3F7', ['Moorea']),('PNG0A4', ['Moorea']),('CHN1D9', ['Kamptonema']),('PAP1D6', ['No 16S']),('ISBH3F3', ['Leptolyngbya']),('PAB3F5', ['Scytolyngbya']),('STM4C5', ['Leptolyngbya'])]

sample_md = pd.DataFrame.from_items(sample_md, columns=['Species'], orient='index')

```


```python
sample_md
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PAL0A1</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>PAL1D4</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>JHB0A2</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>NAK4C8</th>
      <td>Okeania</td>
    </tr>
    <tr>
      <th>3L0A3</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>ASI1E3</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>ASX1E4</th>
      <td>Leptolyngbya</td>
    </tr>
    <tr>
      <th>PNG3F7</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>PNG0A4</th>
      <td>Moorea</td>
    </tr>
    <tr>
      <th>CHN1D9</th>
      <td>Kamptonema</td>
    </tr>
    <tr>
      <th>PAP1D6</th>
      <td>No 16S</td>
    </tr>
    <tr>
      <th>ISBH3F3</th>
      <td>Leptolyngbya</td>
    </tr>
    <tr>
      <th>PAB3F5</th>
      <td>Scytolyngbya</td>
    </tr>
    <tr>
      <th>STM4C5</th>
      <td>Leptolyngbya</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig = bc_pc.plot(sample_md, 'Species',
...                  axis_labels=('PC 1', 'PC 2', 'PC 3'),
...                  title='Samples colored by species', cmap='jet', s=50)
```


![png](output_20_0.png)



```python
toShow = bc_dm.data
ligand = bc_dm.ids
g = pd.DataFrame(toShow,ligand,ligand)
x = seaborn.clustermap(g)
plt.setp(x.ax_heatmap.get_yticklabels(), rotation=0)  # For y axis
plt.setp(x.ax_heatmap.get_xticklabels(), rotation=90) # For x axis
```

    /Users/jasonblues/anaconda/lib/python3.6/site-packages/matplotlib/cbook.py:136: MatplotlibDeprecationWarning: The axisbg attribute was deprecated in version 2.0. Use facecolor instead.
      warnings.warn(message, mplDeprecation, stacklevel=1)





    [None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None]




![png](output_21_2.png)



```python
l= pd.DataFrame(np.matrix(p_axis),ligand)
m = seaborn.clustermap(l)
plt.setp(m.ax_heatmap.get_yticklabels(), rotation=0) 
```

    /Users/jasonblues/anaconda/lib/python3.6/site-packages/matplotlib/cbook.py:136: MatplotlibDeprecationWarning: The axisbg attribute was deprecated in version 2.0. Use facecolor instead.
      warnings.warn(message, mplDeprecation, stacklevel=1)





    [None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     None]




![png](output_22_2.png)



```python

```
