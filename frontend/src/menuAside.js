import {
  mdiAccountCircle,
  mdiMonitor,
  mdiGithub,
  mdiLock,
  mdiAlertCircle,
  mdiSquareEditOutline,
  mdiTable,
  mdiViewList,
  mdiTelevisionGuide,
  mdiResponsive,
  mdiPalette,
  mdiReact,
} from "@mdi/js";

export default [
  {
    to: "/",
    icon: mdiMonitor,
    label: "Dashboard",
  },
  // {
  //   to: "/tables",
  //   label: "Tables",
  //   icon: mdiTable,
  // },
  // {
  //   to: "/forms",
  //   label: "Forms",
  //   icon: mdiSquareEditOutline,
  // },
  {
    to: "/cluster",
    label: "Cluster",
    icon: mdiSquareEditOutline,
  },
  {
    to: "/namespace",
    label: "Namespace",
    icon: mdiSquareEditOutline,
  },
  {
    label: "Workload",
    icon: mdiViewList,
    menu: [
      {
        label: "Pods",
        to: "/pods",
        icon: mdiSquareEditOutline,
      },
      {
        label: "Statefulsets",
      },
      {
        label: "Secrets",
      },
      {
        label: "ConfigMaps",
      },
    ],
  },
  {
    to: "/ui",
    label: "UI",
    icon: mdiTelevisionGuide,
  },
  {
    to: "/responsive",
    label: "Responsive",
    icon: mdiResponsive,
  },
  // {
  //   to: "/",
  //   label: "Styles",
  //   icon: mdiPalette,
  // },
  {
    to: "/profile",
    label: "Profile",
    icon: mdiAccountCircle,
  },
  {
    to: "/login",
    label: "Login",
    icon: mdiLock,
  },
  {
    to: "/error",
    label: "Error",
    icon: mdiAlertCircle,
  },
  {
    label: "Dropdown",
    icon: mdiViewList,
    menu: [
      {
        label: "Item One",
      },
      {
        label: "Item Two",
      },
    ],
  },
  {
    href: "https://github.com/chance-up",
    label: "GitHub",
    icon: mdiGithub,
    target: "_blank",
  },
  // {
  //   href: "https://github.com/chance-up",
  //   label: "React version",
  //   icon: mdiReact,
  //   target: "_blank",
  // },
];
