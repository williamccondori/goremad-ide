export default {
  ssr: false,
  target: "static",
  head: {
    title: "IDE - Gobierno Regional de Madre de Dios",
    htmlAttrs: {
      lang: "es",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: "Gobierno Regional de Madre de Dios",
      },
    ],
    link: [
      { rel: "icon", type: "image/png", href: "/logo.png" },
      {
        rel: "stylesheet",
        href: "https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css",
      },
    ],
    script: [
      {
        src: "https://cdn.jsdelivr.net/npm/leaflet-side-by-side@2.2.0/index.min.js",
      },
    ],
  },
  css: ["@/assets/less/variables.less", "@/assets/css/global.css"],
  plugins: ["@/plugins/ejecutor", "@/plugins/mapa", "@/plugins/ant-modal"],
  loading: true,
  components: true,
  buildModules: [],
  modules: ["@nuxtjs/axios", "@nuxtjs/auth-next"],
  axios: {
    baseURL: process.env.BASE_URL || "http://localhost:8000/api/v1",
  },
  build: {
    hotMiddleware: {
      client: {
        overlay: false,
      },
    },
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
