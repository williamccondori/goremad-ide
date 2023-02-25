export default {
  ssr: false,
  head: {
    title: "GEOGOREMAD",
    htmlAttrs: {
      lang: "es",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "El GEOGOREMAD" },
    ],
    link: [
      { rel: "icon", type: "image/png", href: "/logo.png" },
      {
        rel: "stylesheet",
        href: "https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
      },
    ],
  },
  css: ["@/assets/less/variables.less", "@/assets/css/global.css"],
  plugins: ["@/plugins/antd-ui", "@/plugins/ejecutor", "@/plugins/mapa"],
  loading: false,
  components: false,
  buildModules: [],
  modules: ["@nuxtjs/axios", "@nuxtjs/auth-next"],
  axios: {
    baseURL: process.env.BASE_URL || "http://localhost:8000/api/v1",
  },
  build: {
    loaders: {
      less: {
        lessOptions: {
          javascriptEnabled: true,
        },
      },
    },
  },
  router: {
    middleware: ["auth"],
  },
  auth: {
    redirect: {
      login: "/iniciar-sesion",
      home: "/administrador",
    },
    strategies: {
      local: {
        token: {
          property: "access_token",
        },
        user: { property: false },
        endpoints: {
          login: { url: "/auth/", method: "post" },
          user: { url: "/auth/user/", method: "get" },
          logout: false,
        },
      },
    },
  },
};
