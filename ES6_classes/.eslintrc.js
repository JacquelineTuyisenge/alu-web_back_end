module.exports = {
    env: {
      browser: false,
      es6: true,
      jest: true,
    },
    extends: ['airbnb-base', 'plugin:jest/all'],
    globals: {
      Atomics: 'readonly',
      SharedArrayBuffer: 'readonly',
    },
    parserOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
    },
    plugins: ['jest'],
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': ['error', 'LabeledStatement', 'WithStatement'],
      'no-unused-vars': ['error', { argsIgnorePattern: 'next' }],
      'no-throw-literal': 'error',
      'eol-last': 'error',
      'import/extensions': ['error', 'always', {
        js: 'never',
      }],
    },
    overrides: [
      {
        files: ['*.js'],
        excludedFiles: 'babel.config.js',
        rules: {
          'indent': 'off',
        },
      },
    ],
  };
  