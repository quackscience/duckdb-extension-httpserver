ALL_TYPES_COMPACT = {
    "meta": [
        {"name": "bool", "type": "BOOLEAN"},
        {"name": "tinyint", "type": "TINYINT"},
        {"name": "smallint", "type": "SMALLINT"},
        {"name": "int", "type": "INTEGER"},
        {"name": "bigint", "type": "BIGINT"},
        {"name": "hugeint", "type": "HUGEINT"},
        {"name": "uhugeint", "type": "UHUGEINT"},
        {"name": "utinyint", "type": "UTINYINT"},
        {"name": "usmallint", "type": "USMALLINT"},
        {"name": "uint", "type": "UINTEGER"},
        {"name": "ubigint", "type": "UBIGINT"},
        {"name": "varint", "type": "VARINT"},
        {"name": "date", "type": "DATE"},
        {"name": "time", "type": "TIME"},
        {"name": "timestamp", "type": "TIMESTAMP"},
        {"name": "timestamp_s", "type": "TIMESTAMP_S"},
        {"name": "timestamp_ms", "type": "TIMESTAMP_MS"},
        {"name": "timestamp_ns", "type": "TIMESTAMP_NS"},
        {"name": "time_tz", "type": "TIME WITH TIME ZONE"},
        {"name": "timestamp_tz", "type": "TIMESTAMP WITH TIME ZONE"},
        {"name": "float", "type": "FLOAT"},
        {"name": "double", "type": "DOUBLE"},
        {"name": "dec_4_1", "type": "DECIMAL(4,1)"},
        {"name": "dec_9_4", "type": "DECIMAL(9,4)"},
        {"name": "dec_18_6", "type": "DECIMAL(18,6)"},
        {"name": "dec38_10", "type": "DECIMAL(38,10)"},
        {"name": "uuid", "type": "UUID"},
        {"name": "interval", "type": "INTERVAL"},
        {"name": "varchar", "type": "VARCHAR"},
        {"name": "blob", "type": "BLOB"},
        {"name": "bit", "type": "BIT"},
        {"name": "small_enum", "type": "ENUM('DUCK_DUCK_ENUM', 'GOOSE')"},
        {
            "name": "medium_enum",
            "type": "ENUM('enum_0', 'enum_1', 'enum_2', 'enum_3', 'enum_4', 'enum_5', 'enum_6', 'enum_7', 'enum_8', 'enum_9', 'enum_10', 'enum_11', 'enum_12', 'enum_13', 'enum_14', 'enum_15', 'enum_16', 'enum_17', 'enum_18', 'enum_19', 'enum_20', 'enum_21', 'enum_22', 'enum_23', 'enum_24', 'enum_25', 'enum_26', 'enum_27', 'enum_28', 'enum_29', 'enum_30', 'enum_31', 'enum_32', 'enum_33', 'enum_34', 'enum_35', 'enum_36', 'enum_37', 'enum_38', 'enum_39', 'enum_40', 'enum_41', 'enum_42', 'enum_43', 'enum_44', 'enum_45', 'enum_46', 'enum_47', 'enum_48', 'enum_49', 'enum_50', 'enum_51', 'enum_52', 'enum_53', 'enum_54', 'enum_55', 'enum_56', 'enum_57', 'enum_58', 'enum_59', 'enum_60', 'enum_61', 'enum_62', 'enum_63', 'enum_64', 'enum_65', 'enum_66', 'enum_67', 'enum_68', 'enum_69', 'enum_70', 'enum_71', 'enum_72', 'enum_73', 'enum_74', 'enum_75', 'enum_76', 'enum_77', 'enum_78', 'enum_79', 'enum_80', 'enum_81', 'enum_82', 'enum_83', 'enum_84', 'enum_85', 'enum_86', 'enum_87', 'enum_88', 'enum_89', 'enum_90', 'enum_91', 'enum_92', 'enum_93', 'enum_94', 'enum_95', 'enum_96', 'enum_97', 'enum_98', 'enum_99', 'enum_100', 'enum_101', 'enum_102', 'enum_103', 'enum_104', 'enum_105', 'enum_106', 'enum_107', 'enum_108', 'enum_109', 'enum_110', 'enum_111', 'enum_112', 'enum_113', 'enum_114', 'enum_115', 'enum_116', 'enum_117', 'enum_118', 'enum_119', 'enum_120', 'enum_121', 'enum_122', 'enum_123', 'enum_124', 'enum_125', 'enum_126', 'enum_127', 'enum_128', 'enum_129', 'enum_130', 'enum_131', 'enum_132', 'enum_133', 'enum_134', 'enum_135', 'enum_136', 'enum_137', 'enum_138', 'enum_139', 'enum_140', 'enum_141', 'enum_142', 'enum_143', 'enum_144', 'enum_145', 'enum_146', 'enum_147', 'enum_148', 'enum_149', 'enum_150', 'enum_151', 'enum_152', 'enum_153', 'enum_154', 'enum_155', 'enum_156', 'enum_157', 'enum_158', 'enum_159', 'enum_160', 'enum_161', 'enum_162', 'enum_163', 'enum_164', 'enum_165', 'enum_166', 'enum_167', 'enum_168', 'enum_169', 'enum_170', 'enum_171', 'enum_172', 'enum_173', 'enum_174', 'enum_175', 'enum_176', 'enum_177', 'enum_178', 'enum_179', 'enum_180', 'enum_181', 'enum_182', 'enum_183', 'enum_184', 'enum_185', 'enum_186', 'enum_187', 'enum_188', 'enum_189', 'enum_190', 'enum_191', 'enum_192', 'enum_193', 'enum_194', 'enum_195', 'enum_196', 'enum_197', 'enum_198', 'enum_199', 'enum_200', 'enum_201', 'enum_202', 'enum_203', 'enum_204', 'enum_205', 'enum_206', 'enum_207', 'enum_208', 'enum_209', 'enum_210', 'enum_211', 'enum_212', 'enum_213', 'enum_214', 'enum_215', 'enum_216', 'enum_217', 'enum_218', 'enum_219', 'enum_220', 'enum_221', 'enum_222', 'enum_223', 'enum_224', 'enum_225', 'enum_226', 'enum_227', 'enum_228', 'enum_229', 'enum_230', 'enum_231', 'enum_232', 'enum_233', 'enum_234', 'enum_235', 'enum_236', 'enum_237', 'enum_238', 'enum_239', 'enum_240', 'enum_241', 'enum_242', 'enum_243', 'enum_244', 'enum_245', 'enum_246', 'enum_247', 'enum_248', 'enum_249', 'enum_250', 'enum_251', 'enum_252', 'enum_253', 'enum_254', 'enum_255', 'enum_256', 'enum_257', 'enum_258', 'enum_259', 'enum_260', 'enum_261', 'enum_262', 'enum_263', 'enum_264', 'enum_265', 'enum_266', 'enum_267', 'enum_268', 'enum_269', 'enum_270', 'enum_271', 'enum_272', 'enum_273', 'enum_274', 'enum_275', 'enum_276', 'enum_277', 'enum_278', 'enum_279', 'enum_280', 'enum_281', 'enum_282', 'enum_283', 'enum_284', 'enum_285', 'enum_286', 'enum_287', 'enum_288', 'enum_289', 'enum_290', 'enum_291', 'enum_292', 'enum_293', 'enum_294', 'enum_295', 'enum_296', 'enum_297', 'enum_298', 'enum_299')",
        },
        {"name": "large_enum", "type": "ENUM('enum_0', 'enum_69999')"},
        {"name": "int_array", "type": "INTEGER[]"},
        {"name": "double_array", "type": "DOUBLE[]"},
        {"name": "date_array", "type": "DATE[]"},
        {"name": "timestamp_array", "type": "TIMESTAMP[]"},
        {"name": "timestamptz_array", "type": "TIMESTAMP WITH TIME ZONE[]"},
        {"name": "varchar_array", "type": "VARCHAR[]"},
        {"name": "nested_int_array", "type": "INTEGER[][]"},
        {"name": "struct", "type": "STRUCT(a INTEGER, b VARCHAR)"},
        {"name": "struct_of_arrays", "type": "STRUCT(a INTEGER[], b VARCHAR[])"},
        {"name": "array_of_structs", "type": "STRUCT(a INTEGER, b VARCHAR)[]"},
        {"name": "map", "type": "MAP(VARCHAR, VARCHAR)"},
        {"name": "union", "type": 'UNION("name" VARCHAR, age SMALLINT)'},
        {"name": "fixed_int_array", "type": "INTEGER[3]"},
        {"name": "fixed_varchar_array", "type": "VARCHAR[3]"},
        {"name": "fixed_nested_int_array", "type": "INTEGER[3][3]"},
        {"name": "fixed_nested_varchar_array", "type": "VARCHAR[3][3]"},
        {"name": "fixed_struct_array", "type": "STRUCT(a INTEGER, b VARCHAR)[3]"},
        {"name": "struct_of_fixed_array", "type": "STRUCT(a INTEGER[3], b VARCHAR[3])"},
        {"name": "fixed_array_of_int_list", "type": "INTEGER[][3]"},
        {"name": "list_of_fixed_int_array", "type": "INTEGER[3][]"},
    ],
    "data": [
        [
            False,
            -128,
            -32768,
            -2147483648,
            -9223372036854775808,
            "-170141183460469231731687303715884105728",
            "0",
            0,
            0,
            0,
            0,
            "-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368",
            "5877642-06-25 (BC)",
            "00:00:00",
            "290309-12-22 (BC) 00:00:00",
            "290309-12-22 (BC) 00:00:00",
            "290309-12-22 (BC) 00:00:00",
            "1677-09-22 00:00:00",
            "00:00:00+15:59:59",
            "290309-12-22 (BC) 00:00:00+00",
            -3.4028234663852886e38,
            -1.7976931348623157e308,
            -999.9,
            -99999.9999,
            -1000000000000.0,
            -1e28,
            "00000000-0000-0000-0000-000000000000",
            "00:00:00",
            "🦆🦆🦆🦆🦆🦆",
            "thisisalongblob\\x00withnullbytes",
            "0010001001011100010101011010111",
            "DUCK_DUCK_ENUM",
            "enum_0",
            "enum_0",
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            {"a": None, "b": None},
            {"a": None, "b": None},
            [],
            {},
            "Frank",
            [None, 2, 3],
            ["a", None, "c"],
            [[None, 2, 3], None, [None, 2, 3]],
            [["a", None, "c"], None, ["a", None, "c"]],
            [{"a": None, "b": None}, {"a": 42, "b": "🦆🦆🦆🦆🦆🦆"}, {"a": None, "b": None}],
            {"a": [None, 2, 3], "b": ["a", None, "c"]},
            [[], [42, 999, None, None, -42], []],
            [[None, 2, 3], [4, 5, 6], [None, 2, 3]],
        ],
        [
            True,
            127,
            32767,
            2147483647,
            9223372036854775807,
            "170141183460469231731687303715884105727",
            "340282366920938463463374607431768211455",
            255,
            65535,
            4294967295,
            18446744073709551615,
            "179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368",
            "5881580-07-10",
            "24:00:00",
            "294247-01-10 04:00:54.775806",
            "294247-01-10 04:00:54",
            "294247-01-10 04:00:54.775",
            "2262-04-11 23:47:16.854775806",
            "24:00:00-15:59:59",
            "294247-01-10 04:00:54.775806+00",
            3.4028234663852886e38,
            1.7976931348623157e308,
            999.9,
            99999.9999,
            1000000000000.0,
            1e28,
            "ffffffff-ffff-ffff-ffff-ffffffffffff",
            "83 years 3 months 999 days 00:16:39.999999",
            "goo",
            "\\x00\\x00\\x00a",
            "10101",
            "GOOSE",
            "enum_299",
            "enum_69999",
            [42, 999, None, None, -42],
            [42.0, "nan", "inf", "-inf", None, -42.0],
            ["1970-01-01", "infinity", "-infinity", None, "2022-05-12"],
            ["1970-01-01 00:00:00", "infinity", "-infinity", None, "2022-05-12 16:23:45"],
            ["1970-01-01 00:00:00+00", "infinity", "-infinity", None, "2022-05-12 23:23:45+00"],
            ["🦆🦆🦆🦆🦆🦆", "goose", None, ""],
            [[], [42, 999, None, None, -42], None, [], [42, 999, None, None, -42]],
            {"a": 42, "b": "🦆🦆🦆🦆🦆🦆"},
            {"a": [42, 999, None, None, -42], "b": ["🦆🦆🦆🦆🦆🦆", "goose", None, ""]},
            [{"a": None, "b": None}, {"a": 42, "b": "🦆🦆🦆🦆🦆🦆"}, None],
            {"key1": "🦆🦆🦆🦆🦆🦆", "key2": "goose"},
            5,
            [4, 5, 6],
            ["d", "e", "f"],
            [[4, 5, 6], [None, 2, 3], [4, 5, 6]],
            [["d", "e", "f"], ["a", None, "c"], ["d", "e", "f"]],
            [{"a": 42, "b": "🦆🦆🦆🦆🦆🦆"}, {"a": None, "b": None}, {"a": 42, "b": "🦆🦆🦆🦆🦆🦆"}],
            {"a": [4, 5, 6], "b": ["d", "e", "f"]},
            [[42, 999, None, None, -42], [], [42, 999, None, None, -42]],
            [[4, 5, 6], [None, 2, 3], [4, 5, 6]],
        ],
        [
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
            None,
            None,
        ],
    ],
    "rows": 3,
    "statistics": {"elapsed": 0.06300000101327896, "rows_read": 0, "bytes_read": 0},
}