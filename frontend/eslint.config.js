import globals from "globals";
import js from "@eslint/js";
import prettierConfig from "eslint-config-prettier";
import react from "eslint-plugin-react";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import eslintCss from "@eslint/css";
import eslintJson from "@eslint/json";

export default [
  {
    ignores: ["dist/"],
  },
  js.configs.recommended,
  {
    plugins: {
      json: eslintJson,
    },
  },
  {
    files: ["**/*.{js,jsx}"],
    plugins: {
      react,
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
    },
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: globals.browser,
      parserOptions: {
        ecmaFeatures: {
          jsx: true,
        },
      },
    },
    settings: {
      react: {
        version: "detect",
      },
    },
    rules: {
      ...react.configs.recommended.rules,
      ...reactHooks.configs["recommended-latest"].rules,
      "react-refresh/only-export-components": "warn",
      "no-unused-vars": ["error", { varsIgnorePattern: "^[A-Z_]" }],
      "react/react-in-jsx-scope": "off",
    },
  },
  eslintCss.configs.recommended,
  {
    files: ["**/*.json", "**/*.jsonc"],
    language: "json/jsonc",
    rules: {
      "json/no-duplicate-keys": "error",
      "no-irregular-whitespace": "off",
    },
  },
  prettierConfig,
];
