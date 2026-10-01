import {
  mysqlTable,
  mysqlEnum,
  serial,
  varchar,
  text,
  json,
  timestamp,
} from "drizzle-orm/mysql-core";

// Website form submissions: contact, appointments, enrollment, consultations
export const submissions = mysqlTable("submissions", {
  id: serial("id").primaryKey(),
  type: mysqlEnum("type", ["contact", "appointment", "enrollment", "consultation"]).notNull(),
  name: varchar("name", { length: 255 }).notNull(),
  email: varchar("email", { length: 320 }).notNull(),
  phone: varchar("phone", { length: 64 }),
  payload: json("payload"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export type Submission = typeof submissions.$inferSelect;
export type InsertSubmission = typeof submissions.$inferInsert;

// Chat conversations from the student assistant (for review/improvement)
export const chatLogs = mysqlTable("chat_logs", {
  id: serial("id").primaryKey(),
  lang: varchar("lang", { length: 8 }).notNull().default("en"),
  question: text("question").notNull(),
  answer: text("answer").notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

export type ChatLog = typeof chatLogs.$inferSelect;
