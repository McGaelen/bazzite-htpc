// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
  namespace App {
    // interface Error {}
    // interface Locals {}
    interface PageData {
      config: App.HomepageConfig
    }
    // interface PageState {}
    // interface Platform {}

    interface HomepageConfig {
      links: Array<App.HomepageLink>
    }

    interface HomepageLink {
      url: string
      name: string
      faviconUrl?: string
    }
  }
}

export {}
