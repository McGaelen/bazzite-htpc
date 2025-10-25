<script lang="ts">
  import * as Item from '$lib/components/ui/item/index.js'
  import type { PageProps } from './$types'

  let { data }: PageProps = $props()
</script>

<div class="h-screen w-screen" style="padding: 100px calc(100vw / 7);">
  <Item.Group class="grid grid-cols-3 gap-4">
    {#each data.config.links as model (model.name)}
      <div class="m-auto flex max-w-[200px] flex-wrap">
        <Item.Root variant="default" class="items-center">
          {#snippet child({ props })}
            <a href={model.url} {...props}>
              <Item.Header>
                <img
                  src={model.faviconUrl}
                  alt={model.name}
                  width="128"
                  height="128"
                  class="aspect-square w-full rounded-sm object-cover"
                />
              </Item.Header>
              <Item.Content>
                <Item.Title>{model.name}</Item.Title>
              </Item.Content>
            </a>
          {/snippet}
        </Item.Root>
      </div>
    {/each}
  </Item.Group>
</div>
