import { z } from "zod";
import { createRouter, publicQuery } from "./middleware";
import { getDb } from "./queries/connection";
import { submissions } from "@db/schema";

export const formsRouter = createRouter({
  submit: publicQuery
    .input(
      z.object({
        type: z.enum(["contact", "appointment", "enrollment", "consultation"]),
        name: z.string().min(2).max(255),
        email: z.string().email().max(320),
        phone: z.string().max(64).optional(),
        payload: z.record(z.string(), z.string().max(4000)).optional(),
      }),
    )
    .mutation(async ({ input }) => {
      const db = getDb();
      const result = await db.insert(submissions).values({
        type: input.type,
        name: input.name,
        email: input.email,
        phone: input.phone ?? null,
        payload: input.payload ?? null,
      });
      return { ok: true, id: Number(result[0].insertId) };
    }),
});
