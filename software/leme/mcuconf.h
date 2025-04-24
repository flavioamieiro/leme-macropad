// Copyright 2025 Flavio Amieiro <amieiro.flavio@gmail.com>
// SPDX-License-Identifier: GPL-3.0-only
#pragma once

#include_next <mcuconf.h>

#undef RP_I2C_USE_I2C0
#define RP_I2C_USE_I2C0 TRUE
#undef RP_I2C_USE_I2C1
#define RP_I2C_USE_I2C1 FALSE
