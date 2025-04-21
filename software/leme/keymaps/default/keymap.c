// Copyright 2025 Flavio Amieiro <amieiro.flavio@gmail.com>
// SPDX-License-Identifier: GPL-3.0-only

#include QMK_KEYBOARD_H

enum layers {
  _BASE,
  _NAVIGATION
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┐
     * │ A │ B │ C │
     * ├───┼───┼───┤
     * │ D │ E │ F │
     * └───┴───┴───┘
     */
    [_BASE] = LAYOUT_ortho_2x3(
        KC_F14,    KC_F15,    KC_F16,
        KC_F17,    KC_F18,    TG(_NAVIGATION)
    ),
    [_NAVIGATION] = LAYOUT_ortho_2x3(
        _______, _______, _______,
        _______, _______, TG(_NAVIGATION)
    )
};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
  [_BASE] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU) },
  [_NAVIGATION] = { ENCODER_CCW_CW(MS_WHLU, MS_WHLD) }
};
#endif
