import { createRouter, publicQuery } from "./middleware";
import { formsRouter } from "./forms-router";
import { chatRouter } from "./chat-router";

export const appRouter = createRouter({
  ping: publicQuery.query(() => ({ ok: true, ts: Date.now() })),
  forms: formsRouter,
  chat: chatRouter,
});

export type AppRouter = typeof appRouter;
