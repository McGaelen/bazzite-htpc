import type { PageServerLoad } from './$types'
import { file, $ } from 'bun'
import { env } from '$env/dynamic/private'

export const load: PageServerLoad = async () => {
  let config: App.HomepageConfig = {
    links: [],
  }

  try {
    config = await file(env.HOMEPAGE_CONFIG_LOCATION).json()
  } catch (e) {
    console.error(e)
  }

  return {
    config,
  }
}
