import { createStore } from 'vuex';

export default createStore({
  state: {
    theme: localStorage.getItem('theme') || 'light',
  },
  mutations: {
    toggleTheme(state) {
      state.theme = state.theme === 'light' ? 'dark' : 'light';
      localStorage.setItem('theme', state.theme);
    },
  },
});