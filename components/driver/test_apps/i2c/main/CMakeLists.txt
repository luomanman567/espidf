set(srcs "test_app_main.c"
         "test_i2c.c"
    )

idf_component_register(SRCS ${srcs}
                       PRIV_REQUIRES unity driver test_utils
                       WHOLE_ARCHIVE)
